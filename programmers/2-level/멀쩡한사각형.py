# https://programmers.co.kr/learn/courses/30/lessons/62048
# 멀쩡한 사각형

import math

def solution1(w,h):
    answer = 0
    
    bint, sint = max(w, h), min(w, h)
    lean = bint/sint
    for i in range(sint):
        for k in (math.ceil(i), math.floor(i + lean)):
            answer += 1
    
    answer = w*h - answer
    return answer

def solution(w,h):
    answer = 0
    
    bint, sint = max(w, h), min(w, h)
    lean = bint/sint
    k = 0
    block = 0
    for i in range(1, sint + 1):
        high = round(math.ceil(i*lean), 4)
        low = round(math.floor((i-1)*lean), 4)
        block += round(high - low, 4)
        if (i * lean) % 1 == 0:
            k = i
            break        
    answer = block * (sint//k)
    
    answer = w*h - answer
    return answer


if __name__ == "__main__":
    print(f"solution : {}")