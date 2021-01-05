# 섬연결하기


def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2], reverse=True)
    connected = []
    while len(connected) != n:
        if len(connected) == 0:
            edge = costs.pop()
            connected.append(edge[0])
            connected.append(edge[1])
            answer += edge[2]
        else:
            for i in range(len(costs) - 1, -1, -1):
                if costs[i][0] in connected:
                    if costs[i][1] in connected:
                        costs.pop(i)
                    else:
                        edge = costs.pop(i)
                        connected.append(edge[1])
                        answer += edge[2]
                        break
                elif costs[i][1] in connected:
                    edge = costs.pop(i)
                    connected.append(edge[0])
                    answer += edge[2]
                    break

    return answer
