# 등굣길

# 시간초과
def solution1(m, n, puddles):
    answer = 0

    routes = [[1, 1]]
    while True:
        route = routes.pop()
        if route == [m, n]:
            answer += 1

        if route[0] < m:
            if [route[0] + 1, route[1]] not in puddles:
                routes.append([route[0] + 1, route[1]])

        if route[1] < n:
            if [route[0], route[1] + 1] not in puddles:
                routes.append([route[0], route[1] + 1])

        if len(routes) == 0:
            break
    return answer


def solution(m, n, puddles):
    answer = 0

    xy = [[0 for i in range(m + 1)] for i in range(n + 1)]
    xy[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if [j, i] not in puddles:
                xy[i][j] = xy[i - 1][j] + xy[i][j - 1] + xy[i][j]

    answer = xy[n][m] % 1000000007

    return answer


if __name__ == "__main__":
    print(f"solution : {solution(4, 3, [[2,2]])} ; expected : 4")
