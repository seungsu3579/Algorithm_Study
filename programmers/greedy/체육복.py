# 체육복


def solution(n, lost, reserve):
    answer = n
    tmp = []
    for p in lost:
        if p in reserve:
            tmp.append(p)
    for t in tmp:
        lost.remove(t)
        reserve.remove(t)

    lost.sort()

    for p in lost:
        if p == 1:
            if p + 1 not in reserve:
                answer -= 1
        elif p == n:
            if p - 1 not in reserve:
                answer -= 1
        else:
            if p - 1 in reserve:
                reserve.remove(p - 1)
            # elif p in reserve:
            #     reserve.remove(p)
            elif p + 1 in reserve:
                reserve.remove(p + 1)
            else:
                answer -= 1
    return answer
