# 기능개발
import numpy as np


def solution(progresses, speeds):
    progresses = np.array(progresses)
    speeds = np.array(speeds)
    answer = []
    while True:
        progresses = progresses + speeds
        if progresses[0] >= 100:
            count = 0
            for k in list(progresses):
                if k >= 100:
                    count += 1
                else:
                    break
            progresses = progresses[count:]
            speeds = speeds[count:]
            answer.append(count)
        if len(progresses) == 0:
            break
    return answer
