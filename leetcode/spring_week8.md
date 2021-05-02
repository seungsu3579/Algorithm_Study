# 2021년 4월 5주차

- 기간: 2020/04/26 ~ 2021/05/02
- 푼 문제 수: 3

## 문제

### 1. 3sum ([Link](https://leetcode.com/problems/3sum/))

문제 설명: 3개의 원소 합이 0이 되는 경우를 모두 찾는 것.
분류: array
난이도: Medium
풀이 링크: [Python](https://github.com/seungsu3579/Algorithm_Study/blob/master/leetcode/3Sum.py)
한줄평: nested loop에 의한 모든 경우 탐색은 n^3번의 연산이 필요하지만 이 문제에서는 O(n^2)의 시간 복잡도 안에 풀기를 요구한다. 해시를 통한 인덱스 접근과 3가지 원소값만 필요하다는 점에서 착안하여 문제를 풀었다.

### 2. Letter Combinations of a Phone Number ([Link](https://leetcode.com/problems/letter-combinations-of-a-phone-number/))

문제 설명: 문자열 조합 찾기 문제
분류 : array
난이도: Medium
풀이 링크: [Python](https://github.com/seungsu3579/Algorithm_Study/blob/master/leetcode/letterCombinationsPhoneNumber.py)
한줄평: 단순한 조합 찾기 문제.. 이정도는 그냥해도 되고 itertools라는 라이브러리는 쓰면 더 쉽다.

### 3. Remove Nth Node From End of List ([Link](https://leetcode.com/problems/remove-nth-node-from-end-of-list/))

문제 설명: 링크리스트를 구현하는데 이를 O(n) 시간 복잡도로 삭제 연산을 지원하도록 해야함.
분류: linked list
풀이 링크: [Python](https://github.com/seungsu3579/Algorithm_Study/blob/master/baekjoon/RemoveNthNodeFromEndofList.py)
한줄평 : 딱히 어려움 없이 풀 수 있는 문제였다.
