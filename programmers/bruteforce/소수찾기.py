# 소수찾기


from itertools import permutations, combinations


def solution(numbers):
    numbers = list(map(lambda x: x, numbers))
    all_case = []
    for i in range(1, len(numbers) + 1):
        a = list(permutations(numbers, i))
        all_case += a
    all_case = set(map(lambda x: int("".join(list(x))), all_case))

    answer = 0
    max_num = max(all_case)
    for item in all_case:
        if item == 0 or item == 1:
            continue
        btn = True
        for c in range(2, item // 2 + 1):
            if item % c == 0:
                btn = False
                break
        if btn:
            answer += 1

    return answer
