# 타겟넘버


def recur(num, target, index):
    if index == len(num):
        if target == 0:
            return 1
        else:
            return 0

    a = num[index]
    return recur(num, target + a, index + 1) + recur(num, target - a, index + 1)


def solution(numbers, target):
    answer = recur(numbers, target, 0)
    return answer
