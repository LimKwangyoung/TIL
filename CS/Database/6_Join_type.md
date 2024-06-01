조인(join)이란 두 개 이상의 테이블을 묶어서 하나의 결과물을 만드는 것을 말한다.

***

# 내부 조인
내부 조인(inner join)은 두 테이블의 행 중 모두 일치하는 행이 있는 부분만 표기한다. 두 테이블간의 교집합을 나타낸다.
```sql
SELECT * FROM TableA A
INNTER JOIN TableB B ON
A.key = B.key
```

***

# 왼쪽 조인
왼쪽 조인(left outer join)은 왼쪽 테이블의 모든 행이 결과 테이블에 표기된다. 만약 일치하는 항목이 없으면 해당 값은 null 값이 된다.
```sql
SELECT * FROM Table A
LEFT JOIN TableB B ON
A.key = B.key
```

***

# 오른쪽 조인
오른쪽 조인(right outer join)은 오른쪽 테이블의 모든 행이 결과 테이블에 표기된다. 만약 일치하는 항목이 없으면 해당 값은 null 값이 된다.
```sql
SELECT * FROM Table A
RIGHT JOIN TableB B ON
A.key = B.key
```

***

# 합집합 조인
합집합 조인(full outer join)은 조인 조건에 만족하지 않는 행까지 모두 표기한다. 만약 일치하는 항목이 없으면 누락된 쪽에 null 값이 포함되어 출력된다.
```sql
SELECT * FROM TableA A
FULL OUTER JOIN TableB B ON
A.key = B.key
```

***

# 조인의 종류 심화
![](https://velog.velcdn.com/images/pyoung/post/8bf51b5a-3f26-431b-9752-43ee7e7178b2/image.png)

- **Theta Join** : 비교 조건 `>`, `=`, `<`을 만족하는 조인이다.
- **Equal Join** : 비교 조건 `=`을 만족하는 조인이다.
- **Natural Join** : Equal Join에서 중복 속성을 제거한 조인이다.
- **Inner Join** : 교집합에 해당하는 조인이다.
- **Outer Join** : Inner Join의 결과로 나오지 않는 null 값까지 포함하는 조인이다. Left, Right, Full Outer Join이 있다.

> #### Equal Join $\neq$ Inner Join
Equal Join은 동등 연산자 `=`을 사용한 조인이므로, Inner Join 뿐만 아니라 Outer Join에서도 사용될 수 있다.
