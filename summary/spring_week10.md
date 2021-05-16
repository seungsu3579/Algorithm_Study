# 2021년 5월 2주차

- 기간: 2020/05/10 ~ 2021/05/16
- 푼 문제 수: 3

## 문제

### 1. LCS 문제 ([Link](https://www.acmicpc.net/problem/9251)) - 이번주 추천 문제

문제 설명: LCS문제로 전형적인 DP 문제.
분류: DP
난이도: Medium
풀이 링크: [Python](https://github.com/seungsu3579/Algorithm_Study/blob/master/baekjoon/9251.py)
한줄평: 전형적인 DP문제로 알고리즘만 정확하게 이해한다면 코드는 쉬운편인것 같다.

### 2. Search in Rotated Sorted Array ([Link](https://leetcode.com/problems/search-in-rotated-sorted-array/))

문제 설명: 정렬되었지만 회전된 배열에서 이진 문자열 검색
분류 : binary search
난이도: Medium
풀이 링크: [Python](https://github.com/seungsu3579/Algorithm_Study/blob/master/leetcode/searchInRotatedSortedArray.py)
한줄평: 정렬된 배열에서 이진 검색은 간단한 문제이지만 이 배열이 회전되어 있어 기본적인 이진 검색과는 달랐다. 이때, 배열에서 max 값을 찾기 위해서 O(n)이 아니라 O(logn)으로 max 값을 찾고 mod를 통해 로테이트된 배열에서 이진 검색을 가능하도록 했다.

### 3. Remove Element ([Link](https://leetcode.com/problems/remove-element/))

문제 설명: 링크리스트를 구현하는데 이를 O(n) 시간 복잡도로 삭제 연산을 지원하도록 해야함.
분류: arrary iter
풀이 링크: [Python](https://github.com/seungsu3579/Algorithm_Study/blob/master/leetcode/removeElement.py)
한줄평 : 단순한 iter 문제였는데 파이썬임에도 포인터가 등장하고 코드를 역추적해서 답을 확인하는 방식이라 새로운 배열을 만들어서 하면안됐음...
