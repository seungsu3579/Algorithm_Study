# 2주차 스터디

##

### Heap

- 우선순위큐(Priority Queue): 우선순위가 높은 원소부터 Out되는 큐
- 힙(Heap): 우선순위큐를 위해 만들어진 자료구조로 완전이진트리구조를 띄며 수직 노드간의 정렬은 이뤄져있지만 수평 노드간의 정렬은 이뤄져 있지 않다.
- 종류로는 Max힙, Min힙이 있다.

- 파이썬에서는 heapq 라이브러리를 통해 힙 자료구조를 지원한다.

  ```python
  import heapq

  l = [5,2,6,5,2,1,9,7]
  heapq.heapify(l) # list를 Heap자료구조로 변환  O(N)
  heapq.heappush(l, v) # Min Heap; l리스트에 v값 추가  O(logN)
  heapq.heappush(l, -v) # Max Heap; l리스트에 v값 추가  O(logN)
  heapq.heappop(l) # Heap 자료구조에서 우선순위가 가장 높은 값을 pop
  ```

##

### Sort

- 선택정렬(Selection sort) : O(N^2)

  - 가장 작은 값부터 선택해서 앞으로 옮기며 정렬.
    거품정렬에 비해 2배정도 빠른 알고리즘이지만 더 좋은 알고리즘이 뒤에 있다.

- 삽입정렬(Insertion sort) : O(N^2)

  - 차례로 들어가야할 자리를 찾아서 삽입하며 정렬.
    배열이 작을 때 효율적. >> 팀정렬, 인트로정렬 등 배열이 작을 때 채택되는 알고리즘이기도 함.

- 거품정렬(Bubble sort) : O(N^2)

  - 일반적으로 가장 최악. 정렬되어 있는 경우 가장 빠른 정렬속도를 보인다.

- 힙정렬(Heap sort) : O(NlogN)

  - 힙정렬은 Heap 자료구조를 이용한 정렬으로 Heapify하는데 O(N), Upheap, Downheap에서 O(logN)의 시간 복잡도를 가져 정렬에 있어서 O(NlogN)의 시간복잡도를 갖는 정렬 알고리즘이다.

- 병합정렬(Merge sort) : O(NlogN)

  - 병합정렬은 Devide & Conquer에 충실한 알고리즘으로 재귀로 쉽게 구현하여 정렬할 수 있는 알고리즘이다. Devide는 O(logN)의 시간복잡도가 Conquer는 O(N)의 시간복잡도를 갖고 있어 전체 정렬에 있어 O(NlogN)의 시간복잡도를 갖는다.

- 퀵정렬(Quick sort) : O(NlogN)

  - 퀵정렬도 Devide & Conquer에서 착안한 알고리즘이지만 병합정렬과 다르게 랜덤피벗을 사용한다. 피벗값을 기준으로 큰집단과 작은 집단으로 계속 Devide(O(N))하는 단계를 지나 Conquer(O(logN))단계에서는 순서대로 병합만 이루어진다. 퀵정렬은 확률에 의존하기 때문에 최악의 상황에서 O(N^2)의 시간복잡도를 갖지만 일반적으로는 퀵정렬이 병합과 힙정렬에 비해 빠르다. 병합정렬보다 일반적으로 더 빠르다고 알려져있는데 이는 퀵정렬에서의 Devide가 병합정렬의 Conquer과 비교해서 같은 시간복잡도 O(N)을 갖지만 실제로는 더 빠르기 때문이다.

* 팀정렬(Tim sort)

  - 병합정렬과 삽입정렬을 함께 사용한 하이브리드 정렬 알고리즘. 병합정렬에서 원소가 적을 때 오버헤드가 발생한다는 점을 고려하여 원소가 적을 때 삽입정렬로 오버헤드를 줄이는 방식을 채택한다. 파이썬의 디폴트 정렬 알고리즘. list의 sort()메서드나 sorted 내장함수는 tim sort로 이루어진다.

---

#### <a href="https://programmers.co.kr/learn/courses/30/parts/12117">Heap 문제</a>

#### <a href="https://programmers.co.kr/learn/courses/30/parts/12198">Sort 문제</a>
