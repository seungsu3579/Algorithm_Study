# K번째 수


def solution(array, commands):
    answer = []
    for cmd in commands:
        tmp = array[cmd[0] - 1 : cmd[1]]
        value = sorted(tmp)[cmd[2] - 1]
        answer.append(value)
    return answer
