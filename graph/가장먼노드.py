# 가장 먼 노드


class Node:
    def __init__(self, _id, edges):
        self.id = _id
        self.edges = edges


def solution(n, edge):
    answer = 0
    node = [None]
    searched = [None]
    for i in range(1, n + 1):
        node.append(Node(i, []))
        searched.append(0)
    for e in edge:
        node[e[0]].edges.append(e[1])
        node[e[1]].edges.append(e[0])

    layer_node = [1]
    searched[1] = 1
    count = 1
    while count != n:
        new_layer = []
        for i in layer_node:
            for e in node[i].edges:
                if searched[e] == 0:
                    new_layer.append(node[e].id)
                    searched[node[e].id] = 1
                    count += 1
        layer_node = new_layer
        answer = len(layer_node)
    return answer
