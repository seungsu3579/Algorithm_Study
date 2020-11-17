# 디스크 컨트롤러
import heapq


def solution(jobs):
    jobs = sorted(jobs, key=lambda job: job[0])
    answer = []
    time = 0
    cursor = 0
    finished = 0
    total_job = len(jobs)
    rq = []
    while finished != total_job:
        for i in range(cursor, total_job):
            if time >= jobs[i][0]:
                heapq.heappush(rq, (jobs[i][1], jobs[i][0]))
                cursor = i + 1
            else:
                cursor = i
                break
        if len(rq) == 0:
            time += 1
        else:
            tmp = heapq.heappop(rq)
            time += tmp[0]
            finished += 1
            answer.append(time - tmp[1])
    return int(sum(answer) / len(answer))

