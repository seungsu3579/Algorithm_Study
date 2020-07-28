# 위장


def solution(clothes):
    answer = 1
    closet = dict()
    for cloth in clothes:
        tmp = closet.get(cloth[1], [])
        tmp.append(cloth[0])
        closet[cloth[1]] = tmp

    for kind, items in closet.items():
        answer *= len(items) + 1
    answer -= 1
    return answer
