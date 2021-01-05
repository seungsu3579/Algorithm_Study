# 큰 수 만들기


def solution(number, k):
    flag = 0
    answer = ""
    length = len(number)
    numbers = []
    for i in range(length - 1, -1, -1):
        numbers.append(number[i])

    for n in range(length - 1, 0, -1):
        while numbers[n] < numbers[n - 1]:
            numbers.pop(n)
            flag += 1
            if flag == k or n > len(numbers) - 1:
                break
        if flag == k:
            break

    if flag != k:
        numbers = numbers[k - flag :]
        flag = k

    for l in range(length - k - 1, -1, -1):
        answer += numbers[l]

    return answer
