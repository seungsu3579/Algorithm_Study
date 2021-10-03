# kakao blind test - scenario 2 
from module import *

# grade_gap = 1000 : 235.8133
GRADE_GAP = 1000
ABUSE_POINT_CUT = 3
auth_key = startAPI(problem=2)


# 매칭
def matching():
    userInfo = userInfoAPI(auth_key)
    waitingLine = waitingLineAPI(auth_key)
    userDist = [{'id': dic['id'], 'from': dic['from'], 'grade': userInfo[dic['id']]['grade']} for dic in waitingLine]
    # 점수와 기다린 시간을 기준으로 정렬
    userDist.sort(key=lambda x : (x['grade'], x['from']))

    pairs = []
    idx = 0
    while idx < len(userDist) - 1:
        p1 = userDist[idx]
        p2 = userDist[idx + 1]
        
        if abs(p1['grade'] - p2['grade']) < GRADE_GAP:
            pairs.append([p1['id'], p2['id']])
            idx += 1
        idx += 1

    return pairs


def grade_gap_calc(game):
    time = game["taken"]
    # 플레이어 사이 grade gap 유추
    gap = 9999*((40 - time)/35)
    return gap


# 결과 확인 후 그레이드 설정
def update_grade(userMatchPoint, userAbusePoint):
    # 게임 결과 확인
    game_results = gameResultAPI(auth_key)
    userInfo = userInfoAPI(auth_key) # dict
    commands = list()
    
    # grade 설정
    for game in game_results:
        gap = grade_gap_calc(game)
        winner = userInfo[game['win']]
        loser = userInfo[game['lose']]

        if game['taken'] < 11:
            # abusing 가능성 있음
            if winner['grade'] - loser['grade'] > 8000:
                # 정상적인 게임일 수도
                userMatchPoint[winner['id']].append(winner['grade'])
                userMatchPoint[loser['id']].append(loser['grade'])
            else:
                userAbusePoint[loser['id']] += 1

                if userAbusePoint[loser['id']] > ABUSE_POINT_CUT:
                    # abuser가 있는 게임이라면 점수 반영 X
                    if userAbusePoint[winner['id']] > ABUSE_POINT_CUT:
                        userMatchPoint[winner['id']].append(loser['grade'] - 1000)
                        userMatchPoint[loser['id']].append(winner['grade'] + 1000)
                    else:
                        userMatchPoint[loser['id']].append(winner['grade'] + 2000)
                else:
                    userMatchPoint[winner['id']].append(5000)
                    userMatchPoint[loser['id']].append(3000)


        else:
            if winner['grade'] == 0 or loser['grade'] == 0:
                # 아직 grade가 0일 때
                mean = 4000
            else:
                # grade가 어느정도 자리를 잡았을 때
                mean = (winner['grade'] + loser['grade']) / 2
            
            winnerPoint = min(mean + (gap / 2), 9999)
            loserPoint = max(mean - (gap / 2), 1)
            userMatchPoint[winner['id']].append(winnerPoint)
            userMatchPoint[loser['id']].append(loserPoint)

        winnerDict = {'id': winner['id'], 'grade': sum(userMatchPoint[winner['id']])/len(userMatchPoint[winner['id']])}
        loserDict = {'id': loser['id'], 'grade': sum(userMatchPoint[loser['id']])/len(userMatchPoint[loser['id']])}

        commands += [winnerDict, loserDict]

    return commands


if __name__ == "__main__":

    time = 0
    status = "ready"
    while time <= 595:

        userMatchPoint = dict() # 유저들의 게임 결과를 바탕으로 분포에 따라 주어진 점수 배열
        userAbusePoint = dict() # 어뷰징 유저 경고 횟수
        userInfo = userInfoAPI(auth_key)
        for user in userInfo.keys():
            userMatchPoint[user] = []
            userAbusePoint[user] = 0

        # 게임결과확인 후 grade설정
        commands = update_grade(userMatchPoint, userAbusePoint)
        data = {
            "commands": commands
        }
        changeGradeAPI(data, auth_key)

        # 매칭은 555턴까지 가능
        st = None
        if time <= 555:
            pairs = matching()
            data = {
                "pairs": pairs
            }
            # 매칭 API Call
            st = matchAPI(data, auth_key)
            time = st['time']
        else:
            data = {
                "pairs": []
            }
            matchAPI(data, auth_key)
            time += 1

    print(scoreAPI(auth_key))
