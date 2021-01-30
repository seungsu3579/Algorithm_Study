# https://programmers.co.kr/learn/courses/30/lessons/64065
# 튜플 2019 카카오 개발자 겨울 인턴십


def solution(s):
    answer = []
    tmp = s[1:-1]
    total = []
    flag = True
    for ch in tmp:
        if ch == "{":
            arr = ""
        elif ch == "}":
            total.append(arr)
        else:
            arr += ch

    total = list(map(lambda x: [int(v) for v in x.split(",")], total))
    total.sort(key=lambda x: len(x))

    maps = {}
    for tp in total:
        for v in tp:
            if maps.get(v, False):
                pass
            else:
                maps[v] = True
                answer.append(v)

    return answer


if __name__ == "__main__":
    print(
        f'solution : {solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")} ; expeceted : [2, 1, 3, 4]'
    )
    print(
        f'solution : {solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")} ; expeceted : [2, 1, 3, 4]'
    )
    print(f'solution : {solution("{{20,111},{111}}")} ; expeceted : [111, 20]')
    print(f'solution : {solution("{{123}}")} ; expeceted : [123]')
    print(
        f'solution : {solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")} ; expeceted : [3, 2, 4, 1]'
    )

