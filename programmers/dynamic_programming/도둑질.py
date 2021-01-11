# 도둑질


def solution1(money):
    answer = 0

    targets = [[0, []] for i in range(len(money))]

    for i in range(len(money)):
        if money[i] + targets[i - 2][0] > targets[i - 1][0]:
            if i == len(money) - 1 and targets[i - 2][1][0] == 0:
                targets[i] = targets[i - 1]
                break
            tmp = targets[i - 2][1]
            tmp.append(i)
            targets[i] = [money[i] + targets[i - 2][0], tmp]
        else:
            targets[i] = [targets[i - 1][0], targets[i - 1][1]]

    answer = targets[-1][0]
    return answer


def solution2(money):
    answer = 0

    targets = [[0, []] for i in range(len(money))]

    for i in range(len(money)):
        if money[i] + targets[i - 2][0] > max(
            targets[i - 1][0], money[i] + targets[i - 3][0]
        ):
            if i == len(money) - 1 and targets[i - 2][1][0] == 0:
                targets[i] = targets[i - 1]
                break
            tmp = targets[i - 2][1][:]
            tmp.append(i)
            targets[i] = [money[i] + targets[i - 2][0], tmp]
        elif money[i] + targets[i - 3][0] > max(
            targets[i - 1][0], money[i] + targets[i - 2][0]
        ):
            tmp = targets[i - 3][1][:]
            tmp.append(i)
            targets[i] = [money[i] + targets[i - 3][0], tmp]
        else:
            targets[i] = [targets[i - 1][0], targets[i - 1][1]]
        print(targets)
    answer = targets[-1][0]
    return answer


def solution(money):
    answer = 0

    targets1 = [0 for i in range(len(money))]
    targets2 = [0 for i in range(len(money))]
    targets3 = [0 for i in range(len(money))]
    targets1[0] = money[0]
    targets2[1] = money[1]

    for i in range(2, len(money)):
        if i != len(money) - 1:
            targets1[i] = max(
                money[i] + targets1[i - 3], money[i] + targets1[i - 2], targets1[i - 1]
            )
        else:
            targets1[i] = targets1[i - 1]
        targets2[i] = max(
            money[i] + targets2[i - 3], money[i] + targets2[i - 2], targets2[i - 1]
        )
        targets3[i] = max(
            money[i] + targets3[i - 3], money[i] + targets3[i - 2], targets3[i - 1]
        )

    answer = max(targets2[-1], targets1[-1], targets3[-1])

    return answer


if __name__ == "__main__":
    print(f"solution : {solution([1,2,3,1])} ; expected : 4")
    print(f"solution : {solution([10,2,2,100,2])} ; expected : 110")
    print(f"solution : {solution([1, 1, 4, 1, 4])} ; expected : 8")
