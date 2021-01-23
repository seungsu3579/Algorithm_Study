# 입국심사

# O(klogn)
# 이때 k = 1 billion, n = 100,000 ㅋㅋ 줄여보자 ;;
import heapq


def solution1(n, times):
    answer = 0
    times = list(map(lambda x: (x, x), times))
    heapq.heapify(times)
    while True:
        if n == 0:
            break
        tmp = heapq.heappop(times)
        answer = tmp[0]
        heapq.heappush(times, (tmp[0] + tmp[1], tmp[1]))
        n -= 1

    return answer


import sys


def solution(n, times):
    answer = 0
    left = 0
    right = sys.maxsize * sys.maxsize

    while True:
        person = 0
        time = (left + right) // 2
        for l in times:
            person += time // l

        if person >= n:
            right = time - 1
            answer = time
        elif person < n:
            left = time + 1

        if left > right:
            break

    while True:
        time -= 1
        person = 0
        for l in times:
            person += time // l
        if person >= n:
            answer = time
        else:
            break

    return answer


if __name__ == "__main__":
    print(f"solution : {solution(6, [7, 10])} ; expected : 28")
    # print(f"solution : {solution(10, [1, 5])} ; expected : ")

