# 구명보트


def solution(people, limit):
    answer = 0
    people.sort()

    spt = 0
    bpt = len(people) - 1
    while True:
        if bpt - spt + 1 > 1:
            if people[spt] + people[bpt] <= limit:
                spt += 1
                bpt -= 1
            else:
                bpt -= 1
            answer += 1
        elif bpt - spt + 1 == 1:
            bpt -= 1
            answer += 1
        else:
            break
    return answer
