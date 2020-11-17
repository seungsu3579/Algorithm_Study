# 이중우선순위큐
import heapq


def solution(operation):
    max_heap = []
    min_heap = []
    counter = 0
    for oper in operation:
        cmd, opt = oper.split(" ")
        if counter == 0:
            max_heap = []
            min_heap = []
        if cmd == "I":
            counter += 1
            heapq.heappush(max_heap, (-int(opt), int(opt)))
            heapq.heappush(min_heap, (int(opt), int(opt)))
        elif cmd == "D":
            if counter != 0:
                if opt == "1":
                    counter -= 1
                    heapq.heappop(max_heap)[1]
                elif opt == "-1":
                    counter -= 1
                    heapq.heappop(min_heap)[1]
    if counter == 0:
        answer = [0, 0]
    else:
        answer = [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)[1]]
    return answer
