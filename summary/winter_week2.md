# 2주차 겨울방학 스터디

##

### Q1. dynamic programming 도둑질

[풀이](https://github.com/seungsu3579/Algorithm_Study/tree/master/programmers/dynamic_programming/도둑질.py)

- solution1 : 처음 시도한 코드. 동적프로그래밍의 기본적인 방식으로 풀어봄. 하지만 문제에서 원형으로 데이터가 주어졌기에 처음과 마지막 조건 생성이 까다로움.

- solution2 : 2개의 선택을 건너뛰는 방식으로도 최적이 나올 수 있기에 기존 solution1에서 조건을 추가함... 하지만 여전히 처음과 마지막이 붙어있지 않았을 때를 처리하기 까다로웠음.

- solution : 1번째 집을 선택했을 때와 2번째 집을 처음 선택했을 때, 3번째 집을 처음 선택했을 때의 경우를 나누어 계산. 처음과 마지막이 붙어있지 않아야한다는 조건을 쉽게 처리함.

동적프로그래밍으로 푸는 것도 푸는 것이지만 케이스도 분할하여 진행하여야 해서 조금 더 생각하게 만듬. 더 좋은 코드가 있다면 알려주세용

---

### Q2. dynamic programming 등굣길

[풀이](https://github.com/seungsu3579/Algorithm_Study/tree/master/programmers/dynamic_programming/등굣길.py)

- solution1 : 격자판(n x m)에서 이뤄지길래 graph 형식으로 생각해서 bfs로 품. 하지만 시간 복잡도 측면에서 에러.

- solution : 동적프로그래밍의 기본적인 방식으로 현재 타일으로 올수 있는 경로를 모두 더하는 방식으로 모든 타일을 계산. 시간 복잡도가 O(nm).

처음 접근을 잘못했지만 간단히 풀 수 있는 문제였음.

---

### Q3. dfs-bfs 네트워크

[풀이](https://github.com/seungsu3579/Algorithm_Study/blob/master/programmers/dfs_bfs/네트워크.py)

---

bfs를 while 구문으로 구현하였고 해당 함수로 퍼져 나갈 수 있는 모든 computer들을 set자료구조로 저장해 전체 set에서 차집합을 통해 네트워크로 연결된 computer를 제거 O(n) + O(n). 모든 computer가 체크되면 클러스터 개수를 리턴하도록 함.

set을 통해 더 빠르게 데이터를 제거할 수 있었음. set 관련 메서드의 시간복잡도를 좀더 탐색해보면 좋을 것 같다.
