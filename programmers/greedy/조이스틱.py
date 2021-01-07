# 조이스틱  O


def solution(name):
    answer = 0

    # 상하 움직임 & 좌우 움직임 최적화를 위해 움직이지 않아도 되는 자리수 체크
    stack_list = []
    flag = False

    for i in range(len(name)):
        if name[i] == "A":
            if flag:
                stack_list[-1].append(i)
            else:
                flag = True
                stack_list.append([])
                stack_list[-1].append(i)
        else:
            flag = False
            l1 = abs(ord(name[i]) - ord("A"))
            l2 = 26 - l1
            l = l1 if l2 > l1 else l2
            answer += l

    # A 문자가 적어도 하나 존재할때
    if len(stack_list) != 0:

        tmp = list(map(len, stack_list))
        piv = (
            abs(len(name) - stack_list[tmp.index(max(tmp))][-1]) - 1
            if stack_list[tmp.index(max(tmp))][0] - 1
            > abs(len(name) - stack_list[tmp.index(max(tmp))][-1]) - 1
            else stack_list[tmp.index(max(tmp))][0] - 1
        )

        if stack_list[0][0] == 0 or stack_list[-1][-1] == len(name) - 1:
            loop = (
                len(name)
                - 1
                - max(
                    [
                        len(stack_list[0] if stack_list[0][0] == 0 else []),
                        len(
                            stack_list[0] if stack_list[-1][-1] == len(name) - 1 else []
                        ),
                    ]
                )
            )
        else:
            loop = len(name) - 1

        horizontal = min([loop, len(name) - max(tmp) + piv - 1,])

        answer += horizontal

    else:
        answer += len(name) - 1

    return answer


if __name__ == "__main__":

    print(f"solution = {solution('AABAABAAAAAABAAABAA')}")
    print(f"solution = {solution('JEROEN')}")
    print(f"solution = {solution('JAN')}")
