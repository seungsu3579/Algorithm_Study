# https://programmers.co.kr/learn/courses/30/lessons/1845
# 폰켓몬


def solution(nums):
    answer = 0
    tmp = set(nums)
    answer = len(tmp) if len(tmp) <= len(nums) // 2 else len(nums) // 2
    return answer
