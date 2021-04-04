# https://www.acmicpc.net/problem/1937
import sys

sys.setrecursionlimit(40000)


def solution():
    n = int(input())

    total_node = []
    matrix = []
    for i in range(n):
        line = [int(j) for j in input().split()]
        matrix.append([Node(i, j, line[j]) for j in range(len(line))])

    for i in range(n):
        for j in range(n):
            if i != 0 and matrix[i][j].value < matrix[i - 1][j].value:
                matrix[i][j].addEdge(matrix[i - 1][j])

            if i != len(matrix) - 1 and matrix[i][j].value < matrix[i + 1][j].value:
                matrix[i][j].addEdge(matrix[i + 1][j])

            if j != 0 and matrix[i][j].value < matrix[i][j - 1].value:
                matrix[i][j].addEdge(matrix[i][j - 1])

            if j != len(matrix) - 1 and matrix[i][j].value < matrix[i][j + 1].value:
                matrix[i][j].addEdge(matrix[i][j + 1])

            total_node.append(matrix[i][j])

    for i in range(n):
        for j in range(n):
            if len(matrix[i][j].reverse) == 0:
                search(matrix[i][j], 1)

    answer = 0
    for node in total_node:
        if node.count > answer:
            answer = node.count

    return answer


def search(node, count):
    if node == None:
        return

    if node.count <= count:
        node.count = count
    else:
        return

    for n in node.edges:
        search(n, count + 1)


class Node:
    def __repr__(self):
        return f"({self.x}, {self.y} : {self.value} | {self.count})"

    def __init__(self, i, j, value):
        self.x = i
        self.y = j
        self.value = value
        self.count = 0
        self.edges = []
        self.reverse = []

    def addEdge(self, node):
        if node not in self.edges:
            self.edges.append(node)
            node.reverse.append(self)


if __name__ == "__main__":
    a = solution()
    print(a)
