# 카펫


def solution(brown, yellow):
    answer = []
    brown_case = []
    b = (brown + 4) // 2
    for k in range(2, b // 2 + 1):
        brown_case.append((k, b - k))
        if (k - 2) * (b - k - 2) == yellow:
            return [b - k, k]

