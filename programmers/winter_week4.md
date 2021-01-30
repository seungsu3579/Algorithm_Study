# 3주차 겨울방학 스터디

##

### Q1. dfs/bfs 여행경로

[풀이](https://github.com/seungsu3579/Algorithm_Study/tree/master/programmers/dfs_bfs/여행경로.py)

- solution : dfs로 품. node class를 정의해서 graph 자료구조를 구현. 그저 지나온 길을 체크해두고 오면서 탐색하면 금방 찾음.

이때 같은 티켓이 여러장 있을 수 있는데 이때 길을 체크할 때 여러장을 체크하지 않으면 정확성 테스트1에서 실패. 엣지케이스를 생각하기 어려웠지만 막상 듣고보면 쉬운 문제였음.

---

### Q2. binary_search 입국심사

[풀이](https://github.com/seungsu3579/Algorithm_Study/tree/master/programmers/binary_search/입국심사.py)

- solution1 : 시간복잡도가 문제;; O(klogn)이지만 k가 1 billion, n이 100,000이다. 다시 작성할 필요가 있음.<br>
  <img src="./img/입국심사_s1.png" height="200">

- solution : 시간을 지정했을 때, 그 때의 처리한 사람 수를 알 수 있다.(O(n)) 따라서 가능한 시간을 binary search하게 움직여 가능한 조건을 만족하는 시간을 찾는다. 이 방법으로도 애를 먹었는데 그 시간에 처리한 사람 조건은 `n보다 크거나 같다` 이지만 `== n` 이라고 잘못 생각해서 시간이 좀 걸렸다.

문제 조건을 보고 인사이트를 가질 수 있도록 해야겠다. 입국심사를 기다리는 사람이 10억이면 바로 log(10억)으로 처리할 수 있는 로직을 생각해보도록 하자.

---

### Q3. binary_search 징검다리

[풀이](https://github.com/seungsu3579/Algorithm_Study/blob/master/programmers/binary_search/징검다리.py)

---

- solution1 : 논리적인 접근이 잘못된듯 하다. 예외 케이스를 찾았지만 해결방법을 찾지는 못했다. 다른 방식의 접근이 필요해보인다. 길이가 10억까지 제시될 수 있는데 Q2에서 풀었던 방식과 비슷하게 접근하려했지만 쉽지 않았다...
