# 모의고사


def solution(answers):
    p1 = "12345"
    p2 = "21232425"
    p3 = "3311224455"
    score = [0, 0, 0]
    for a in range(len(answers)):
        if str(answers[a]) == p1[a % len(p1)]:
            score[0] += 1
        if str(answers[a]) == p2[a % len(p2)]:
            score[1] += 1
        if str(answers[a]) == p3[a % len(p3)]:
            score[2] += 1

    answer = []
    max_num = max(score)
    for k in range(3):
        if score[k] == max_num:
            answer.append(score.index(max_num) + 1)
            score[score.index(max_num)] = -1

    return answer
