# https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3
# 124 나라의 숫자


def solution(n):
    answer = ""

    answer = recur(answer, n - 1)

    return answer


def recur(answer, n):
    int_map = {1: "2", 2: "4", 0: "1"}
    mk = n // 3
    rm = n % 3

    answer = int_map[rm] + answer

    if mk == 0:
        return answer
    else:
        answer = recur(answer, mk - 1)

    return answer


if __name__ == "__main__":

    print(f"solution : {solution(1)} ; expected : 1")
    print(f"solution : {solution(2)} ; expected : 2")
    print(f"solution : {solution(3)} ; expected : 4")
    print(f"solution : {solution(4)} ; expected : 11")
    print(f"solution : {solution(5)} ; expected : 12")
    print(f"solution : {solution(6)} ; expected : 14")
    print(f"solution : {solution(7)} ; expected : 21")
    print(f"solution : {solution(8)} ; expected : 22")
    print(f"solution : {solution(9)} ; expected : 24")
    print(f"solution : {solution(10)} ; expected : 41")
