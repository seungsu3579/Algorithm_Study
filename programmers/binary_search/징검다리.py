# 징검다리
import heapq


def solution1(distance, rocks, n):
    answer = 0

    points = rocks[:] + [0, distance]
    points.sort()

    prev = 0
    tmp = []
    for p in range(1, len(points)):
        tmp.append(points[p] - prev)
        prev = points[p]

    for i in range(n):
        idx = tmp.index(min(tmp))

        if idx == 0:
            tmp = [sum(tmp[0:2])] + tmp[2:]
        elif idx == len(tmp) - 1:
            tmp = tmp[:-2] + [sum(tmp[-2:])]
        else:
            if tmp[idx + 1] > tmp[idx - 1]:
                tmp = tmp[: idx - 1] + [sum(tmp[idx - 1 : idx + 1])] + tmp[idx + 1 :]
            else:
                tmp = tmp[:idx] + [sum(tmp[idx : idx + 2])] + tmp[idx + 2 :]

    answer = min(tmp)

    return answer


def solution(distance, rocks, n):
    answer = 0
    return answer


if __name__ == "__main__":

    print(f"solution : {solution1(25, [2, 14, 11, 21, 17], 2)} ; expected : 4")
    print(f"solution : {solution1(16, [4, 8, 11], 2)} ; expected : 8")
