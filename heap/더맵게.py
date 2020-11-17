# 더 맵게
import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K and len(scoville) != 1:
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        new = min1 + min2 * 2
        heapq.heappush(scoville, new)
        answer += 1
    if len(scoville) == 1:
        if scoville[0] < K:
            return -1
    return answer
