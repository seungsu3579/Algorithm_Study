# https://programmers.co.kr/learn/courses/30/lessons/60057
# 문자열 압축


def solution(s):
    answer = 0
    answer_list = []

    for n in range(1, len(s) // 2 + 2):
        tmp = compression2(s, n)
        answer_list.append(len(tmp))

    answer = min(answer_list)

    return answer


def compression2(s, n):
    subset = []
    compressed_str = ""
    i = 0
    prev = ""
    count = 1
    while i <= len(s):
        target = s[i : i + n]
        if prev == target:
            count += 1
        else:
            if count == 1:
                compressed_str += prev
            else:
                compressed_str += f"{count}{prev}"
            prev = target
            count = 1
        i += n

    compressed_str += s[i - n :]

    return compressed_str


def compression(s, n):
    comp_dict = {}
    compressed_str = ""
    i = 0
    while i <= len(s) - n:
        target = s[i : i + n]

        idx = i + 2 * n
        count = 1
        # check duplicated str
        while idx <= len(s):
            if target == s[idx - n : idx]:
                count += 1
                idx += n
            else:
                break

        # write compressed str
        if count == 1:
            compressed_str += s[i]
            i += 1
        else:
            compressed_str += f"{count}{target}"
            i += count * n

    compressed_str += s[i:]

    return compressed_str


if __name__ == "__main__":
    print(f"solution : {solution('a')} ; expected : 1")
    print(f"solution : {solution('aabbaccc')} ; expected : 7")
    print(f"solution : {solution('ababcdcdababcdcd')} ; expected : 9")
    print(f"solution : {solution('abcabcdede')} ; expected : 8")
    print(f"solution : {solution('abcabcabcabcdededededede')} ; expected : 14")
    print(f"solution : {solution('xababcdcdababcdcd')} ; expected : 17")
