# 인덱스의 필요성
인덱스는 데이터를 빠르게 찾을 수 있는 하나의 장치이다. 인덱스를 설정하면 테이블 안에 내가 찾고자 하는 데이터를 빠르게 찾을 수 있다.

***

# B-트리
인덱스는 B-트리 자료 구조로 이루어져 있다. B-트리는 이진 트리를 확장해 하나의 노드가 가질 수 있는 자식 노드의 최대 숫자가 2보다 큰 트리 구조이다. 이는 루트 노드, 리프 노드, 그리고 루트 노드와 리프 노드 사이에 있는 브랜치 노드로 나뉜다. B-트리는 인덱스 키를 바탕으로 항상 정렬된 상태를 유지한다.

해당 예시를 보자.
트리 탐색은 맨 위 루트 노드부터 탐색이 일어나며 브랜치 노드를 거쳐 리프 노드까지 내려온다. 처음 루트 노트에서는 39, 83 이후 아래 노드로 내려와 46, 53, 57 등 정렬된 값을 기반으로 탐색하는 것을 볼 수 있다.

인덱스에는 B-트리에서 발전된 B+트리를 더 자주 활용한다. B+트리는 리프 노드에만 key-value를 저장하고, 리프 노드끼리는 연결 리스트로 구성되어 있는 트리이다. B-트리보다 B+트리를 활용하는 이유는, 인덱스 컬럼은 부등호를 이용한 순차 검색 연산이 자주 발생하기 때문이다.

### 인덱스가 효율적인 이유와 대수확장성
인덱스가 효율적인 이유는 효율적인 단계를 거쳐 모든 요소에 접근할 수 있는 균형 잡힌 트리 구조와 트리 깊이의 대수확장성 때문이다.

대수 확장성이란 트리 깊이가 리프 노드 수에 비해 매우 느리게 성장하는 것을 의미한다. 기본적으로 인덱스가 한 깊이씩 증가할 때마다 최대 인덱스 항목의 수는 4배씩 증가하기 때문에, 적은 깊이로도 많은 레코드를 검색할 수 있다.

***

# 인덱스 만드는 방법
### MySQL
MySQL은 클러스터형 인덱스와 세컨더리 인덱스가 있다.

클러스터형 인덱스는 테이블당 하나를 설정할 수 있다. `primary key` 옵션으로 기본키로 만들면 클러스터형 인덱스를 생성할 수 있고, 기본키로 만들지 않고 `unique not null` 옵션을 붙이면 클러스터형 인덱스로 만들 수 있다. 하나의 인덱스만 생성할 것이라면 클러스터형 인덱스를 만드는 것이 성능이 더 좋다.

세컨터리 인덱스는 `create index...` 명령어를 기반으로 만들 수 있다. 세컨더리 인덱스는 보조 인덱스로 여러 개의 필드 값을 기반으로 쿼리를 많이 보낼 때 생성해야 하는 인덱스이다.

### MongoDB
MongoDB의 경우 도큐먼트를 만들면 자동으로 ObjectID가 형성되며, 해당 키가 기본키로 설정된다. 그리고 세컨더리키도 부가적으로 설정해서 기본키와 세컨더리키를 같이 쓰는 복합 인덱스를 설정할 수 있다.

***

# 인덱스 최적화 방법
### 1. 인덱스는 비용이다.
인덱스는 두 번 탐색하도록 강요한다. 우선 인덱스 리스트에서 해당 값이 저장된 위치를 찾는다. 그리고 인덱스 리스트에서 찾은 위치를 바탕으로 컬렉션에서 데이터를 찾는다. 이는 관련 읽기 비용이 든다.

또한 컬렉션이 수정되었을 때 인덱스도 수정되어야 한다. 이때 B-트리의 높이를 균형 있게 조절하는 비용도 들고, 데이터를 효율적으로 조회할 수 있도록 분산시키는 비용도 든다.

따라서 쿼리에 있는 필드에 인덱스를 무작정 다 설정하는 것은 답이 아니며, 컬렉션에서 가져와야 하는 양이 많을수록 인덱스를 사용하는 것은 비효율적이다.

### 2. 항상 테스팅하라.
인덱스 최적화 기법은 서비스 특징에 따라 달라진다. 서비스에서 사용하는 객체의 깊이, 테이블의 양 등이 다르기 때문이다. 따라서 항상 테스팅하는 것이 중요하다. MySQL에서는 다음과 같은 코드로 테스팅을 수행한다.
```sql
EXPLAIN
SELECT * FROM t1
JOIN t2 ON t1.c1 = t2.c1
```

### 3. 복합 인덱스는 같음, 정렬, 다중 값, 카디널리티 순이다.
복합 인덱스를 생성할 때는 순서가 있고, 생성 순서에 따라 인덱스 성능이 달라진다. 같음, 정렬, 다중 값, 카디널리티 순으로 생성해야 한다.

1. `==`이나 `equal`이라는 쿼리가 있다면 제일 먼저 인덱스로 설정한다.
2. 정렬에 쓰는 필드라면 그다음 인덱스로 설정한다.
3. `>` 또는 `<` 등 다중 값을 출력해야 하는 필드라면 나중에 인덱스를 설정한다.
4. 카디널리티가 높은 순서를 기반으로 인덱스를 생성한다.