# 순위


class Node:
    def __init__(self, _id):
        self.id = _id
        self.up = []
        self.down = []


def countNode(node, _id, searched, up):
    baseNode = node[_id]
    queue = [_id]
    count = 0
    while len(queue) != 0:
        i = queue.pop()
        if up:
            direction = node[i].up
        else:
            direction = node[i].down
        for e in direction:
            if searched[e] == 0:
                queue.append(e)
                searched[e] = 1
                count += 1
    return count


def solution(n, results):
    answer = 0
    node = [None]
    searched = [None]
    for i in range(1, n + 1):
        node.append(Node(i))
        searched.append(0)
    for e in results:
        node[e[0]].down.append(e[1])
        node[e[1]].up.append(e[0])

    for i in range(1, n + 1):
        up = countNode(node, i, searched, True)
        down = countNode(node, i, searched, False)
        for i in range(1, n + 1):
            searched[i] = 0
        if up + down == n - 1:
            answer += 1
    return answer
