## 1주차 스터디

- python의 list 자료구조의 slicing은 O(n) 시간복잡도를 가짐.

---

### Hash

- 해쉬(Hash): 임의 Key값을 고정 길이로 변환하는 것
- 해쉬 테이블(Hash Table): Key값의 연산을 통해 직접 메모리에 접근이 가능한 데이터 구조
- 해싱 함수(Hashing Function): Key에 대해 산술 연산을 이용해 데이터(Value) 위치를 찾을 수 있는 함수
- Key를 해싱 함수로 연산해서, 해쉬 주소를 알아내고, 이를 기반으로 해쉬 테이블에서 해당 Key에 대한 데이터 위치를 일관성있게 알 수 있음

- _dictionary_ 자료구조
  - 파이썬의 내장된 자료구조인 dict는 해시 기반으로 동작하여 짧은 시간복잡도로 메모리에 대한 접근이 가능하다. 하지만 규모가 커지면 비효율적으로 동작하게 되므로 유의해서 사용하자.

---

### stack, queue

- 스택(Stack): LIFO(Last In First Out)에 따라 동작하는 자료구조
- 큐(Queue): FIFO(First In First Out)에 따라 동작하는 자료구조

- collections 라이브러리를 활용하면 더 효율적인 코딩이 가능

  - _Deque_ : 큐의 앞과 뒤에서 삽입 삭제가 가능한 큐

    - stack, queue 구현
      | 종류 | list() | collections.deque() |
      | ----- | ---------------- | -------------------- |
      | Stack | pop() , append() | pop() , append() |
      | Queue | pop(0), append() | pop() , appendleft() |

    - 효율성
      - list는 배열로 구현되어 pop()함수가 index가 주어졌을 때 해당 index의 원소를 지우고 list 전체의 원소를 한칸씩 움직여 시간복잡도가 높음.
      - 반면에 collections의 deque의 경우 원형 연결리스트로 구현되어 있어 삭제가 이뤄지더라도 모든 원소를 한칸씩 움직이는 비효율적인 연산을 할 필요가 없음. 그렇기에 삽입과 삭제가 자유로움.

  - _OrderedDict_ : 순서가 존재하는 dictionary이기에 정렬이 가능

    ```python
    from collections import OrderedDict

    d = dict()
    d['x'], d['y'], d['z'] = 100, 300, 200

    order_dict = OrderedDict(sorted(d.items(), key=lambda t:t[0]))
    ```

  - _defaultdict_ : dictionary의 변수를 생성시에 기본 key값을 지정할 수 있는 자료구조

    ```python
    from collections import defaultdict
    # 디폴트 값을 0으로 설정
    d = defaultdict(lambda:0)

    # 디폴트 값을 리스트로 지정
    d = defaultdict(list)
    ```

  - _Counter_ : 시퀀스 자료형의 데이터 요소 개수를 dictionary 형태로 변환하는 자료구조

  - _namedtuple_ : 데이터 구조체를 저장하는 자료구조 (C의 구조체와 유사)

---

#### <a href="https://programmers.co.kr/learn/courses/30/parts/12077">Hash 문제</a>

#### <a href="https://programmers.co.kr/learn/courses/30/parts/12081">Stack, Queue 문제</a>
