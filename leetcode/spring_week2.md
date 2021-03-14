# 2021년 3월 2주차

- 기간: 2020/03/08 ~ 2021/03/14
- 푼 문제 수: 3

## 문제

### 1. Shortest To Char (동영 추천 문제) ([Link](https://leetcode.com/problems/shortest-distance-to-a-character/))

문제 설명: 주어진 string에서 주어진 char의 가장 가까운 index와 현재 index의 거리에 따른 배열을 리턴하는 문제
분류: array
난이도: Easy
풀이 링크: [Python](https://github.com/seungsu3579/Algorithm_Study/blob/master/leetcode/shortestToChar.py)
한줄평: 동영이가 추천한 문제. abs 메서드를 통해 구현하면 양방향 탐색으로 쉽게 풀수 있음. 하지만 시간 복잡도를 고려하여 한방향 탐색하는 대신 이전 char의 위치를 기록하여 O(n)으로 품.

### 2. Two Sum ([Link](https://leetcode.com/problems/two-sum/))

문제 설명: 주어진 배열에서 2가지 원소의 합이 주어진 integer가 되는 조합의 index를 리턴하는 문제
분류: math
난이도: Easy
풀이 링크: [Python](https://github.com/seungsu3579/Algorithm_Study/blob/master/leetcode/twosum.py)
한줄평: 그냥 조합! 음... 조합이다.

### 3. Add Two Numbers ([Link](https://leetcode.com/problems/add-two-numbers/))

분류: linked list
난이도: Medium
풀이 링크: [Python](https://github.com/seungsu3579/Algorithm_Study/blob/master/leetcode/addTwoNumbers.py)
한줄평: linked list의 특성을 알고 포인터를 잘 옮겨주면 쉽게 풀수 있다. 올림수가 있어 자리 수가 증가할 경우를 놓쳤지만 해당 케이스를 찾기는 쉬웠다. 그냥 그런 문제.
