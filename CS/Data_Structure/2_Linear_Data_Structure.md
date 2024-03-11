선형 자료 구조란 요소가 일렬로 나열되어 있는 자료 구조를 말한다.

# 연결 리스트
연결 리스트는 데이터를 감싼 노드를 포인터로 연결해서 공간적인 효율성을 극대화시킨 자료 구조이다. 삽입과 삭제가 $O(1)$이 걸리며, 탐색에는 $O(n)$이 걸린다.

![](https://velog.velcdn.com/images/pyoung/post/b61f2180-c03e-4ffd-8aa5-80a585537325/image.png)

`prev` 포인터와 `next` 포인터로 앞과 뒤의 노드를 연결시킨 것을 연결 리스트라고 하며, 싱글 연결 리스트, 이중 연결 리스트, 원형 이중 연결 리스트가 있다. 그리고 맨 앞에 있는 노드를 헤드(head)라고 한다.

- **싱글 연결 리스트** : `next` 포인터만 가진다.
- **이중 연결 리스트** : `next` 포인터와 `prev` 포인터를 가진다.
- **원형 이중 연결 리스트** : 이중 연결 리스트와 같지만 마지막 노드의 `next` 포인터가 헤드 노드를 가리킨다.

이중 연결 리스트는 앞에서부터 요소를 넣는 `push_front()`, 뒤에서부터 요소를 넣는 `push_back()`, 중간에 요소를 넣는 `insert()` 등의 함수가 있다.
```c
#include <bits/stdc++.h>
using namespace std;
int main() {
	list<int> a;
    for (int i = 0; i < 10; i++)a.push_back(i);
    for (int i = 0; i < 10; i++)a.push_front(i);
    auto it = a.begin(); it++;
    a.insert(it, 1000);
    for (auto it : a) cout << it << " ";
    cout << '\n';
    a.pop_front();
    a.pop_back();
    for (auto it : a) cout << it << " ";
    cout << '\n';
    return 0;
}
/*
9 1000 8 7 6 5 4 3 2 1 0 0 1 2 3 4 5 6 7 8 9
1000 8 7 6 5 4 3 2 1 0 0 1 2 3 4 5 6 7 8
*/    
```

# 배열
배열(array)은 같은 타입의 변수들로 이루어져 있고, 크기가 정해져 있으며, 인접한 메모리 위치에 있는 데이터를 모아놓은 집합이다. 중복을 허용하고 순서가 있다.

접근(참조)에 $O(1)$의 시간 복잡도를 가지며 랜덤 접근(random access)이 가능하다. 삽입과 삭제에는 $O(n)$이 걸린다. 따라서 데이터 추가와 삭제를 많이 하는 것은 연결 리스트, 접근(참조)를 많이 하는 것은 배열로 하는 것이 좋다.

> 여기서 배열은 '정적 배열'을 의미한다.

### 랜덤 접근과 순차적 접근
직접 접근이라고 하는 랜덤 접근은 임의의 인덱스에 해당하는 데이터에 접근할 수 있는 기능이다. 이는 데이터를 저장된 순서대로 검색해야 하는 순차적 접근과 반대이다.
![](https://velog.velcdn.com/images/pyoung/post/80746037-5467-499a-b882-6a2980ac4c32/image.png)

### 배열과 연결 리스트 비교
![](https://velog.velcdn.com/images/pyoung/post/abac30a5-3d6b-402d-a78a-9fd9dc23ad33/image.png)

접근(참조)은 배열이 빠르고 연결 리스트가 느리다. 배열은 $n$번째 요소를 그저 접근(참조)하면 되기 때문에 $O(1)$의 시간 복잡도를 가진다. 연결 리스트는 포인터를 기반으로 순차적으로 이동해야 하기 때문에 $O(n)$의 시간 복잡도를 가진다. 즉, 참조가 많이 일어나는 작업의 경우 배열이 빠르고 연결 리스트는 느리다.

데이터 추가 및 삭제는 연결 리스트가 빠르고 배열이 느리다. 배열은 모든 데이터를 옮겨야 추가가 가능하지만, 연결 리스트는 포인터를 바꾸어 연결하면 되기 때문이다.

```c
#include <bits/stdc++.h>
using namespace std;
int a[10];
int main() {
	for (int i = 0; i < 10; i++)a[i] = i;
    for (auto it : a) cout << it << " ";
    cout << '\n';
    return 0;
}
/*
0 1 2 3 4 5 6 7 8 9
*/
```

# 벡터
벡터(vector)는 동적으로 요소를 할당할 수 있는 동적 배열이다. 중복을 허용하고 순서가 있으며 랜덤 접근이 가능하다. 탐색과 맨 뒤의 요소를 삭제하거나 삽입하는 데 $O(1)$이 걸리며, 맨 뒤가 아닌 요소를 삭제하거나 삽입하는 데 $O(n)$의 시간이 걸린다.

참고로 포인터를 이용해 접근하기 때문에 배열보다 느리다.

![](https://velog.velcdn.com/images/pyoung/post/831676af-6e00-4a91-9b56-2a2574c45792/image.png)

위의 그림처럼 `push_back()`을 한다고 해서 매번 크기가 증가하는 것이 아니라 2의 제곱승 + 1마다 크기를 2배로 늘리는 것을 알 수 있다.

$c_i$를 $i$번째 `push_back()`을 할 때 드는 비용(cost)라고 하면, $c_i$는 $1$ 또는 $1 + 2^k$이다. 따라서 $n$번 `push_back()`을 한다고 했을 때 드는 비용 $T(n)$은 다음과 같다.
$T(n)=\sum\limits_{i=0}^n c_i \leq n+\sum\limits_{i=0}^{log_{2}n}2^i = n+2n-1=3n-1$
이를 $n$으로 나누게 되면 `push_back()`을 할 때 평균적으로 드는 비용을 알 수 있는데, 이는 $3$이다. $1$이라는 상수 시간보다는 크지만 상수 시간에 가까운 amortized 복잡도를 가진다는 것을 알 수 있다.
```c
#include <bits/stdc++.h>
using namespace std;
vector<int> v;
int main() {
	for (int i = 1; i <= 10; i++)v.push_back(i);
    for (int a : v) cout << a << " ";
    cout << "\n";
    v.pop_back();
    
    for (int a : v) cout << a << " ";
    cout << "\n";
    
    v.erase(v.begin(), v.begin() + 1);
    
    for (int a : v) cout << a << " ";
    cout << "\n";
    
    auto a = find(v.begin(), v.end(), 100);
    if (a == v.end()) cout << "not found" << "\n";
    
    fill(v.begin(), v.end(), 10);
    for (int a : v) cout << a << " ";
    cout << "\n";
    v.clear();
    for (int a : v) cout << a << " ";
    cout << "\n";
    
    return 0;
}
/*
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9
2 3 4 5 6 7 8 9
not found
10 10 10 10 10 10 10 10
*/
```

# 스택
스택(stack)은 가장 마지막으로 들어간 데이터가 가장 첫 번째로 나오는 성질(LIFO, Last In First Out)을 가진 자료 구조이다. 재귀적인 함수, 알고리즘에 사용되며 웹 브라우저 방문 기록 등에 쓰인다. 삽입 및 삭제에 $O(1)$, 탐색에 $O(n)$이 걸린다.
![](https://velog.velcdn.com/images/pyoung/post/6297a100-c0a9-43ab-a503-5e51cf2b1130/image.png)

```c
#include <bits/stdc++.h>
using namespace std;
stack<int> stk;
int main() {
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    for (int i = 0; i < 10; i++)stk.push(i);
    while (stk.size()) {
    	cout << stk.top() << " ";
        stk.pop();
	}
}
/*
9 8 7 6 5 4 3 2 1 0
*/
```

# 큐
큐(queue)는 먼저 집어넣은 데이터가 먼저 나오는 성질(FIFO, First In First Out)을 지닌 자료 구조이다. 삽입 및 삭제에 $O(1)$, 탐색에 $O(n)$이 걸린다. CPU 작업을 기다리는 프로세스, 스레드 행렬 또는 네트워크 접속을 기다리는 행렬, 너비 우선 탐색, 캐시 등에 사용된다.
```c
#include <bits/stdc++.h>
using namespace std;
int main() {
	queue<int> q;
    q.push(1);
    cout << q.front() << "\n";
    q.pop();
    cout << q.size() << "\n";
    return 0;
}
/*
1
0
*/
```
 참고로 C++에서 `enqueue()`는 `push()`, `dequeue()`는 `pop()`으로 구현되어 있다.