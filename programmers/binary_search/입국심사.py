# 입국심사

import heapq

# O(klogn)
# 이때 k = 1 billion, n = 100,000 ㅋㅋ 줄여보자 ;;
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


if __name__ == "__main__":
    print(f"solution : {solution(6, [7, 10])} ; expected : 28")

