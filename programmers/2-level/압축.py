# https://programmers.co.kr/learn/courses/30/lessons/17684
# 압축


def solution(msg):
    answer = []

    maps = dict(map(lambda x: (str(chr(x + 64)), x), [i + 1 for i in range(26)]))
    num = 26

    idx = 0
    gap = 1
    while True:
        substring = msg[idx : idx + gap]

        if maps.get(substring, False):
            gap += 1

            if idx + gap > len(msg):
                answer.append(maps.get(substring))
                break

        else:
            num += 1
            maps[substring] = num
            answer.append(maps.get(substring[:-1]))
            idx = idx + gap - 1
            gap = 1

    return answer


if __name__ == "__main__":
    print(f"solution : {solution('KAKAO')} ; expected : [11, 1, 27, 15]")
    print(
        f"solution : {solution('TOBEORNOTTOBEORTOBEORNOT')} ; expected : [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]"
    )
    print(
        f"solution : {solution('ABABABABABABABAB')} ; expected : [1, 2, 27, 29, 28, 31, 30]"
    )

