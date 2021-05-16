# 2021년 4월 1주차

- 기간: 2020/03/29 ~ 2021/04/04
- 푼 문제 수: 3

## 문제

### 1. Container With Most Water ([Link](https://leetcode.com/problems/container-with-most-water/))

문제 설명: 리스트로 기둥의 높이가 주어졌을때 물을 담을 수 있는 최대 넓이를 구하는 문제
분류: array
난이도: Medium
풀이 링크: [C++](https://github.com/seungsu3579/Algorithm_Study/blob/master/leetcode/containerWithMostWater.cpp)
한줄평: 기본적으로 모든 경우를 찾으려고 하면 시간복잡도가 높아 통과할 수 없음. O(n^2)가 아니라 O(n)으로 풀어야하는 문제. 높은 기둥을 기준으로 범위를 줄여나가면서 넓이를 선형 탐색해야함.

### 2. Integer to Roman ([Link](https://leetcode.com/problems/integer-to-roman/))

문제 설명: 주어진 int 형의 num을 Roman 숫자형태로 바꾸는 문제
분류 : string
난이도: Medium
풀이 링크: [C++](https://github.com/seungsu3579/Algorithm_Study/blob/master/leetcode/integerToRoman.cpp)
한줄평: medium 문제지만 어려운 테크닉을 요구하지는 않음. 그냥 분기만 잘 나누면 됨.

### 3. 욕심쟁이 판다 - 추천문제 ([Link](https://www.acmicpc.net/problem/1937))

문제 설명: 주어진 정방행렬에서 판다가 이동할 수 있는 최장 루트를 찾는 문제. 다음 경로의 value가 무조건 현재 value보다 높아야 이동 가능.
분류: DP? DFS?
풀이 링크: [Python](https://github.com/seungsu3579/Algorithm_Study/blob/master/baekjoon/1937.py)
한줄평: DP, DFS 어떤 방식으로 풀어야할지 고민하다가 쉬운 DFS로 풀었는데 시간 초과가 남. DP로 다시 풀어야하는데 시간이 없네요..ㅎㅎ
