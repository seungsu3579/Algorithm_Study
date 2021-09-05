# 5주차 스터디

##

### Dynamic Programming(동적계획법)

재귀적으로 생각하기, 불필요한 계산 줄이기, 점화식, 순환식

- 재귀적으로 생각하기

  - 작은 문제는 해결되어 있다는 믿음을 가지고 큰 문제를 해결하는 방법

- 불필요한 계산 줄이기

  - Memoization(메모이제이션) : 중간 결과를 메모리에 저장해 불러옴. Top-down 방식

  - Bottom-up(밑에서부터 계산하기) : 재귀에 의한 오버헤드가 없음

ex) 이항계수, 피보나치