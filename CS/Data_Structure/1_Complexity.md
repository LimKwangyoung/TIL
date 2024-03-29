자료 구조(data structure)는 효율적으로 관리, 수정, 삭제, 탐색, 저장할 수 있는 데이터 집합을 말한다. C++은 STL을 기반으로 전반적인 자료 구조를 가장 잘 설명할 수 있는 언어이다.

> #### 용어
**STL** : C++의 표준 템플릿 라이브러리이자 스택, 배열 등 데이터 구조의 함수 등을 제공하는 라이브러리의 묶음

# 복잡도
### 시간 복잡도
#### 빅오 표기법
시간 복잡도란 '입력 크기에 대해 어떠한 알고리즘이 실행되는 데 걸리는 시간'이다. 주요 로직의 반복 횟수를 중점으로 측정되며, 보통 빅오 표기법으로 나타낸다. 예를 들어 '입력 크기 $n$'의 모든 입력에 대한 알고리즘에 필요한 시간이 $10n^2+n$이라고 하면 다음과 같이 코드를 작성할 수 있다.
```c
for (int i = 0; i < 10; i++) {
	for (int j = 0; j < n; j++) {
    	for (int k = 0; k < n; k++) {
        	if (true) cout << k << '\n';
		}
	}
}
for (int i = 0; i < n; i++) {
	if (true) cout << i << '\n';
}
```

빅오 표기법이란 입력 범위 $n$을 기준으로 로직이 몇 번 반복되는지를 나타내는데, '가장 영향을 많이 끼치는' 항의 상수 인자를 빼고 나머지 항을 없앤 것이다. 증가 속도를 고려하여 다른 항들의 영향을 생각하지 않는다. 따라서 앞선 예시의 시간 복잡도는 $O(n^2)$라고 할 수 있다.

#### 시간 복잡도의 존재 이유
시간 복잡도는 효율적인 코드로 개선하는 데 쓰이는 척도이다.

#### 시간 복잡도의 속도 비교
![](https://velog.velcdn.com/images/pyoung/post/d47d1866-964a-4d7b-b3f9-b8af25dcc12b/image.png)

### 공간 복잡도
공간 복잡도는 프로그램을 실행시켰을 때 필요로 하는 자원 공간의 양을 의미한다.

### 자료 구조에서의 시간 복잡도
보통 시간 복잡도를 생각할 때, 평균과 최악의 시간 복잡도를 고려하여 사용한다.

#### 자료 구조의 평균 시간 복잡도
|자료 구조|접근|탐색|삽입|삭제|
|---|---|---|---|---|
|배열(array)|$O(1)$|$O(n)$|$O(n)$|$O(n)$|
|스택(stack)|$O(n)$|$O(n)$|$O(1)$|$O(1)$|
|큐(queue)|$O(n)$|$O(n)$|$O(1)$|$O(1)$|
|이중 연결 리스트(doubly linked list)|$O(n)$|$O(n)$|$O(1)$|$O(1)$|
|해시 테이블(hash table)|$O(1)$|$O(1)$|$O(1)$|$O(1)$|
|이진 탐색 트리(BST)|$O(logn)$|$O(logn)$|$O(logn)$|$O(logn)$|
|AVL 트리|$O(logn)$|$O(logn)$|$O(logn)$|$O(logn)$|
|레드 블랙 트리|$O(logn)$|$O(logn)$|$O(logn)$|$O(logn)$|

#### 자료 구조의 최악 시간 복잡도
|자료 구조|접근|탐색|삽입|삭제|
|---|---|---|---|---|
|배열(array)|$O(1)$|$O(n)$|$O(n)$|$O(n)$|
|스택(stack)|$O(n)$|$O(n)$|$O(1)$|$O(1)$|
|큐(queue)|$O(n)$|$O(n)$|$O(1)$|$O(1)$|
|이중 연결 리스트(doubly linked list)|$O(n)$|$O(n)$|$O(1)$|$O(1)$|
|해시 테이블(hash table)|$O(n)$|$O(n)$|$O(n)$|$O(n)$|
|이진 탐색 트리(BST)|$O(n)$|$O(n)$|$O(n)$|$O(n)$|
|AVL 트리|$O(logn)$|$O(logn)$|$O(logn)$|$O(logn)$|
|레드 블랙 트리|$O(logn)$|$O(logn)$|$O(logn)$|$O(logn)$|