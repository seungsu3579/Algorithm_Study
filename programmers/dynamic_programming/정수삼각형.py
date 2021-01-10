# 정수 삼각형


def solution(triangle):
    answer = 0

    routes = triangle[-1]
    for i in range(2, len(triangle) + 1):
        nodes = triangle[-i]
        tmp = []

        for j in range(len(nodes)):
            tmp.append(
                nodes[j] + routes[j]
                if routes[j] > routes[j + 1]
                else nodes[j] + routes[j + 1]
            )
        routes = tmp

    answer = routes[0]

    return answer


if __name__ == "__main__":
    print(
        f"solution : {solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])} ; expected : 30"
    )

