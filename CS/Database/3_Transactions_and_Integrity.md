# 트랜잭션
트랜잭션은 데이터베이스에서 하나의 논리적 기능을 수행하기 위한 작업의 단위이다. 여러 개의 쿼리들을 하나로 묶는 단위를 말하며, 원자성, 일관성, 독립성, 지속성의 특징을 갖고 있다.

### 원자성
*"all or nothing"*

원자성(atomicity)은 트랜잭션과 관련된 일이 모두 수행되었거나 되지 않았거나를 보장하는 특징이다.

또한 트랜잭션 단위로 여러 로직들을 묶을 때 외부 API를 호출하는 것이 있으면 안된다. 만약 있다면 롤백이 일어났을 때 어떻게 해야 할 것인지에 대한 해결 방법이 있어야 한다.

#### 커밋과 롤백
커밋(commit)은 여러 쿼리가 성공적으로 처리되었다고 확정하는 명령어이다. 트랜잭션 단위로 수행되며 변경된 내용이 모두 영구적으로 저장되는 것을 말한다.

롤백(rollback)이란 에러나 여러 이슈 때문에 트랜잭션으로 처리한 하나의 묶음 과정을 일어나기 전으로 돌리는 일(취소)을 말한다.

커밋과 롤백 덕에 데이터의 무결성이 보장된다. 또한 데이터 변경 전에 변경 사항을 쉽게 확인할 수 있고 해당 작업을 그룹화할 수 있다.

#### 트랜잭션 전파
트랜잭션을 수행할 때 커넥션 단위로 수행하기 때문에 커넥션 객체를 넘겨서 수행해야 한다. 이를 매번 넘기지 않고, 여러 트랜잭션 관련 메서드의 호출을 하나의 트랜잭션에 묶이도록 하는 것을 트랜잭션 전파라고 한다.

> #### 용어
**커넥션** : 애플리케이션과 데이터베이스 서버 간의 통신 링크이다.

### 일관성
일관성(consistency)은 '허용된 방식'으로만 데이터를 변경해야 하는 것을 의미한다. 데이터베이스에 기록된 모든 데이터는 여러 가지 조건, 규칙에 따라 유효함을 가진다.

### 격리성
격리성(isolation)은 트랜잭션 수행 시 서로 끼어들지 못하는 것을 말한다. 복수의 병렬 트랜잭션은 서로 격리되어 마치 순차적으로 실행되는 것처럼 작동되어야 하며, 데이터베이스는 여러 사용자가 같은 데이터에 접근할 수 있어야 한다.

격리성은 여러 개의 격리 수준으로 나뉘어 격리성을 보장한다.

#### 격리 수준
**SERIALIZABLE**
SERIALIZABLE은 트랜잭션을 순차적으로 진행시키는 것을 말한다. 여러 트랜잭션이 동시에 같은 행에 접근할 수 없다. 이 수준은 매우 엄격한 수준으로 교착 상태가 일어날 확률이 많고 가장 성능이 떨어진다.

**REPEATABLE_READ**
REPEATABLE_READ는 하나의 트랜잭션이 수정한 행을 다른 트랜잭션이 수정할 수 없도록 막아주지만 새로운 행을 추가하는 것은 막지 않는다.

**READ_COMMITTED**
READ_COMMITTED는 커밋 완료된 데이터에 대해서만 조회를 허용한다. 또한 어떤 트랜잭션이 접근한 행을 다른 트랜잭션이 수정할 수 있다. 이 때문에 같은 행을 다시 읽을 때 다른 내용이 발견될 수 있다.

**READ_UNCOMMITTED**
READ_UNCOMITTED는 가장 낮은 격리 수준으로, 하나의 트랜잭션이 커밋되기 이전에 다른 트랜잭션에 노출되는 문제가 있지만 가장 빠르다. 이는 데이터 무결성을 위해 사용하지 않는 것이 이상적이지만, '어림잡아' 집계하는 데에 사용하면 좋다.

#### 격리 수준에 따라 발생하는 현상
REPEATABLE_READ은 팬텀 리드, READ_COMMITTED는 팬텀 리드, 반복 가능하지 않은 조회, READ_UNCOMMITTED는 팬텀 리드, 반복 가능하지 않은 조회, 더티 리드가 발생할 수 있다.

**팬텀 리드**
팬텀 리드(phantom read)는 한 트랜잭션 내에서 동일한 쿼리를 보냈을 때 해당 조회 결과가 다른 경우를 말한다.

**반복 가능하지 않은 조회**
반복 가능하지 않은 조회(non-repeatable read)는 한 트랜잭션 내의 같은 행에 두 번 이상 조회가 발생했는데, 그 값이 다른 경우를 말한다.

팬텀 리드와 다른 점은 반복 가능하지 않은 조회는 행 값이 달라질 수도 있는데, 팬텀 리드는 다른 행이 선택될 수도 있다는 것을 의미한다.

**더티 리드**
더티 리드(dirty read)는 한 트랜잭션이 수행 중일 때 다른 트랜잭션에 의해 수정되었지만 아직 '커밋되지 않은' 행의 데이터를 읽을 수 있을 때 발생한다.

### 지속성
지속성(durability)은 성공적으로 수행된 트랜잭션은 영원이 반영되어야 하는 것을 의미한다. 이는 원래 상태로 복구하는 회복 기능이 있어야 함을 뜻하며, 이를 위해 체크섬, 저널링, 롤백 등의 기능을 제공한다.

> #### 용어
**체크섬** : 중복 검사의 한 형태로, 오류 정정을 통해 송신된 자료의 무결성을 보호하는 단순한 방법이다.
**저널링** : 변경 사항을 반영(commit)하기 전에 로깅하는 것으로, 트랜잭션 등 변경 사항에 대한 로그를 남기는 것이다.

***

# 무결성
데이터의 정확성, 일관성, 유효성을 유지하는 것을 말하며, 무결성이 유지되어야 데이터베이스의 신뢰가 생긴다.

|이름|설명|
|---|---|
|개체 무결성|기본키로 선택된 필드는 빈 값을 허용하지 않는다.|
|참조 무결성|서로 참조 관계에 있는 두 테이블의 데이터는 항상 일관된 값을 유지해야 한다.|
|고유 무결성|특정 속성에 대해 고유한 값을 가지도록 조건이 주어진 경우 그 속성 값은 모두 고유한 값을 가진다.|
|NULL 무결성|특정 속성 값에 NULL이 올 수 없다는 조건이 주어진 경우 그 속성 값은 NULL이 될 수 없다는 제약 조건이다.|