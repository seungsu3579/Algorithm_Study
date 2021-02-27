def maxCost(cost, labels, dailyCount):

    answer = []
    count = 0
    c = 0
    for i in range(len(cost)):
        if labels[i] == "legal":
            count += 1

        c += cost[i]

        if count == dailyCount:
            count = 0
            answer.append(c)
            c = 0

    if len(answer) == 0:
        return 0
    else:
        return max(answer)
