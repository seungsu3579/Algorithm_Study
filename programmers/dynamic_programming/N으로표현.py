# N으로 표현


class pack:
    def __init__(self, num, weight):
        self.num = num
        self.weight = weight


def solution(N, number):
    answer = 0

    # knapsack [sum, weight]
    ns = [[i, 0] for i in range(number + 1)]

    # kinds of load
    case = [{"num": int(str(N) * i), "weight": i} for i in range(1, 6)]
    case += [{"num": int(str(1) * i), "weight": i + 1} for i in range(1, 6)]
    print(case)

    return answer


if __name__ == "__main__":
    print(f"solution : {solution(5, 12)} ; expected 4")
    print(f"solution : {solution(2, 11)} ; expected 3")
