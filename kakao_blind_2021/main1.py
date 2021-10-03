# kakao blind test - scenario 1
from module import *

# grade_gap = 2100 : 249.694
GRADE_GAP = 2100
auth_key = startAPI(problem=1)


# 매칭
def matching():
    userInfo = userInfoAPI(auth_key)
    waitingLine = waitingLineAPI(auth_key)
    userDist = [{'id': dic['id'], 'from': dic['from'], 'grade': userInfo[dic['id']]['grade']} for dic in waitingLine]
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
    gap = 9999*((40 - time)/35)
    return gap


# 결과 확인 후 그레이드 설정
def update_grade(userMatchPoint):
    # 게임 결과 확인
    game_results = gameResultAPI(auth_key)
    userInfo = userInfoAPI(auth_key) # dict
    commands = list()
    
    # grade 설정
    for game in game_results:
        gap = grade_gap_calc(game)
        winner = userInfo[game['win']]
        loser = userInfo[game['lose']]

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

        userMatchPoint = dict()
        userInfo = userInfoAPI(auth_key)
        for user in userInfo.keys():
            userMatchPoint[user] = []
        
        # 게임결과확인 후 grade설정
        commands = update_grade(userMatchPoint)
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
