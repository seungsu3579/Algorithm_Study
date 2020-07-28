# 탑


def solution(heights):
    index = len(heights) - 1
    answer = []
    for k in range(len(heights)):
        answer.append(0)

    for k in range(len(heights)):
        for m in range(0, k + 1):
            if heights[k] < heights[m]:
                answer[k] = m + 1

    return answer
