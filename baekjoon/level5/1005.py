# ACM Craft
# 아 모르겠다ㅠㅜ 왜 다익스트라로는 안되는거야;;

import heapq


class Node:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight
        self.time = 123456
        self.prev = []

    def setNext(self, node):
        self.prev.append(node)

    def __repr__(self):
        return f"node{self.id}"

    def __lt__(self, other):
        return self.time < other.time

    def __eq__(self, other):
        return self.time == other.time


def solution(nodes, target):

    nodes[target].time = nodes[target].weight
    heap = list(nodes.values())
    heapq.heapify(heap)

    while True:
        if len(heap) == 0:
            break

        # 힙에서 노드 가져오기
        node = heapq.heappop(heap)

        if node.time == 123456:
            break

        # 노드에서 갈 수 있는 노드를 탐색 후 힙에 포함
        for src in node.prev:
            if src.time == 123456:
                src.time = node.time + src.weight
            else:
                if node.time + src.weight > src.time:
                    src.time = node.time + src.weight

        heapq.heapify(heap)

    answer = 0
    for node in list(nodes.values()):
        if node.time != 123456 and node.time > answer:
            answer = node.time

    return answer


if __name__ == "__main__":

    test_num = int(input())

    graphs = list()
    answers = []

    for k in range(test_num):
        N, K = input().split()

        nodes = dict()
        weight = input().split()
        for i in range(int(N)):
            nodes[i + 1] = Node(i + 1, int(weight[i]))

        for i in range(int(K)):
            edge = input().split()
            nodes[int(edge[1])].setNext(nodes[int(edge[0])])

        target = int(input())
        answer = solution(nodes, target)

        answers.append(answer)

    for a in answers:
        print(a)
