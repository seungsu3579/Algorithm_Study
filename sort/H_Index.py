# H-Index


def solution(citations):
    answer = 0
    tmp = sorted(citations, reverse=True)
    paper_num = len(tmp)
    for h in range(1, paper_num + 1):
        if tmp[h - 1] >= h:
            if h == paper_num:
                answer = h
            elif tmp[h] <= h:
                answer = h
    return answer
