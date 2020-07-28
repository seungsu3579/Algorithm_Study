# 라면공장
import heapq


def solution(stock, dates, supplies, k):
    answer = 0
    sub = []
    cursor = 0
    l = len(dates)
    while stock < k:
        for i in range(cursor, l):
            if dates[i] <= stock:
                print(f"추가 : {supplies[i]}")
                heapq.heappush(sub, -supplies[i])
                cursor = i + 1
            else:
                cursor = i
                break
        stock -= heapq.heappop(sub)
        answer += 1
        print(f"stock : {stock}")

    return answer
