# 여행경로


class Node:
    def __init__(self, port):
        self.port = port
        self.edges = []
        self.size = 0
        self.check = dict()

    def addEdge(self, node):
        self.edges.append(node)
        self.check[node.port] = self.check.get(node.port, [])
        self.check[node.port].append(True)
        self.size += 1

    def sort(self):
        self.edges.sort(key=lambda node: node.port)

    def __repr__(self):
        return (
            f"{self.port} > {list(map(lambda x : x.port, self.edges))} : {self.check}"
        )


def solution(tickets):
    def explore(route, src):
        if len(route) == len(tickets) + 1:
            return route

        src.sort()
        for dst in src.edges:
            if src.check[dst.port]:
                route.append(dst.port)
                src.check[dst.port].pop()
                explore(route, dst)

                if len(route) == len(tickets) + 1:
                    return route
                else:
                    route.pop()
                    src.check[dst.port].append(True)

    answer = []

    g = dict()
    airports = list(set(sum(tickets, [])))
    for airport in airports:
        g[airport] = Node(airport)

    for ticket in tickets:
        g[ticket[0]].addEdge(g[ticket[1]])

    answer = explore(["ICN"], g["ICN"])

    return answer


if __name__ == "__main__":
    print(
        f"solution : {solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']])} ; expected = [ICN, JFK, HND, IAD]"
    )
    print(
        f"solution : {solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']])} ; expected = [ICN, ATL, ICN, SFO, ATL, SFO]"
    )
    print(
        f"solution : {solution([['ICN', 'A'],['ICN', 'A'],['ICN', 'A'],['A', 'ICN'],['A', 'ICN']])} ; expected = [ICN, A, ICN, A, ICN, A]"
    )

