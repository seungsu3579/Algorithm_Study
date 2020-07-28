# 프린터


def solution(priorities, location):
    jobs = len(priorities)
    answer = 0
    cursor = 0
    while True:
        if max(priorities) == priorities[cursor % jobs]:
            priorities[cursor % jobs] = 0
            answer += 1
            if cursor % jobs == location:
                break
        cursor += 1
    return answer
