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

- solution :

처음 접근을 잘못했지만 간단히 풀 수 있는 문제였음.

---

### Q3. dfs-bfs 네트워크

[풀이](https://github.com/seungsu3579/Algorithm_Study/blob/master/programmers/dfs_bfs/네트워크.py)

---

bfs를 while 구문으로 구현하였고 해당 함수로 퍼져 나갈 수 있는 모든 computer들을 set자료구조로 저장해 전체 set에서 차집합을 통해 네트워크로 연결된 computer를 제거 O(n) + O(n). 모든 computer가 체크되면 클러스터 개수를 리턴하도록 함.

set을 통해 더 빠르게 데이터를 제거할 수 있었음. set 관련 메서드의 시간복잡도를 좀더 탐색해보면 좋을 것 같다.
