# 가장 큰 수


def solution(numbers):
    num_list = []
    for num in numbers:
        s = str(num)
        tmp_s = s * 4
        new_s = tmp_s[:4]
        num_list.append((new_s, s))
    num_list = sorted(num_list, key=lambda num: num[0], reverse=True)
    answer = ""
    for num in num_list:
        answer += num[1]
    if answer[0] == "0":
        answer = "0"
    return answer
