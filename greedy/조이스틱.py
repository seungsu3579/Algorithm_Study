# 조이스틱  X


def solution(name):
    answer = 0
    for i in range(len(name)):
        l1 = abs(ord(name[i]) - ord("A"))
        l2 = 26 - l1
        l = l1 if l2 > l1 else l2
        print(l)
        answer += l

    right = 0
    while name[right + 1] == "A":
        right += 1
    left = 0
    while name[-1 - left] == "A":
        left += 1
    rl = right if right > left else left

    answer += len(name) - rl - 1

    return answer
