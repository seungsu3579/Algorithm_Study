# https://programmers.co.kr/learn/courses/30/lessons/64061
# 2019 카카오 겨울 인턴십 : 크레인 인형 뽑기 게임


def solution(board, moves):
    answer = 0
    stack = []

    prev = -1
    for cont in moves:
        cont -= 1
        # pick
        doll = 0
        for b in board:
            if b[cont] != 0:
                doll = b[cont]
                b[cont] = 0
                break
        if doll == 0:
            continue

        if len(stack) != 0:
            if stack[-1] == doll:
                stack.pop()
                answer += 2
            else:
                stack.append(doll)
        else:
            stack.append(doll)

    return answer


if __name__ == "__main__":
    print(
        f"solution : {solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])} / expected : 4"
    )

