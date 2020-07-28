# 주식가격


def solution(prices):
    answer = []
    for k in range(len(prices)):
        count = -1
        for p in range(k, len(prices)):
            count += 1
            if prices[p] < prices[k]:
                break
        answer.append(count)
    return answer
