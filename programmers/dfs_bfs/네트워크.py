# 네트워크


def solution(n, computers):
    def bfs(stack, check):
        group = set()
        while True:
            if len(stack) == 0:
                break

            target = stack.pop()
            for i in range(n):
                if computers[target][i] == 1 and not check[i]:
                    group.add(i)
                    stack.append(i)
                    check[i] = True
        return group

    answer = 0
    nodes = {i for i in range(n)}

    while True:

        if len(nodes) == 0:
            break

        answer += 1
        check = [False for i in range(n)]
        target = nodes.pop()
        group = bfs([target], check)

        nodes -= group

    return answer


if __name__ == "__main__":
    print(f"solution : {solution(3, [[1,1,0],[1,1,0],[0,0,1]])} ; expected : 2")
    print(f"solution : {solution(3, [[1,1,0],[1,1,1],[0,1,1]])} ; expected : 1")
