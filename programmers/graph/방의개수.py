# 방의 개수

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.edges = []
        self.searched = []

def draw(picture, cursor, arrow):
    direction = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    x = cursor.x + direction[arrow][0]
    y = cursor.y + direction[arrow][1]
    if picture.get((x, y), None) == None:
        node = Node(x, y)
        picture[(x, y)] = node
    else:
        node = picture[(x, y)]
    cursor.edges.append(node)
    return node

def solution(arrows):
    answer = 0
    base = Node(0,0)
    cursor = base
    picture = {(0,0): base}
    for a in arrows:
        newNode = draw(picture, cursor, a)
        cursor = newNode
        if len(newNode.edges) != 0:
            answer += 1  
    return answer
