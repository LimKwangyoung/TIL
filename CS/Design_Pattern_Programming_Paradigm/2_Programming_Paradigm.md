프로그래밍 패러다임(programming paradigm)은 프로그래머에게 프로그래밍의 관점을 갖게 해주는 역할을 하는 개발 방법론이다. 프로그래밍 패러다임은 크게 선언형, 명령형으로 나누며, 선언형은 함수형이라는 하위 집합을 갖는다. 또한, 명령형은 다시 객체지향, 절차지향으로 나뉜다.
![](https://velog.velcdn.com/images/pyoung/post/4527ef6a-1ad9-4e76-b23a-a47b6a0ea0b6/image.png)

***

# 선언형과 함수형 프로그래밍
선언형 프로그래밍(declarative programming)이란 '무엇을' 풀어내는가에 집중하는 패러다임이며, "프로그램은 함수로 이루어진 것이다."라는 명제가 담겨 있다. 함수형 프로그래밍(functional programming)은 선언형 패러다임의 일종이다.

배열에서 최댓값을 찾는 로직은 다음과 같다.
```js
const list = [1, 2, 3, 4, 5, 11 ,12]
const ret = list.reduce((max, num) => num > max ? num : max, 0)
console.log(ret)  // 12
```
함수형 프로그래밍은 이와 같이 작은 '순수 함수'들을 블록처럼 쌓아 로직을 구현하고 '고차 함수'를 통해 재사용성을 높인 프로그래밍 패러다임이다. 대표적으로 자바스크립트가 있다.

### 순수 함수
출력이 입력에만 의존하는 것을 의미한다.
```js
const pure = (a, b) => {
  return a + b
}
```
매개 변수 `a`, `b` 말고 다른 전역 변수 `c` 등이 출력에 영향을 주면 순수 함수가 아니다.

### 고차 함수
함수가 함수를 값처럼 매개변수로 받아 로직을 생성할 수 있는 것을 말한다.

#### 일급 객체
고차 함수를 쓰기 위해서는 해당 언어가 일급 객체라는 틍직을 가져야 한다.

- 변수나 메서드에 함수를 할당할 수 있다.
- 함수 안에 함수를 매개변수로 담을 수 있다.
- 함수가 함수를 반환할 수 있다.

함수형 프로그래밍은 이외에도 커링, 불변성 등의 특징이 있다.

> #### 용어
**커링** : 인자를 여러 개 받는 함수를 분리하여, 인자를 하나씩만 받는 함수의 체인으로 만든다. 함수의 재사용성이 높아진다.

***

# 객체지향 프로그래밍
객체지향 프로그래밍(OOP, Object-Oriented Programming)은 객체들의 집합으로 프로그램의 상호 작용을 표현하며 데이터를 객체로 취급하여 내부에 선언된 메서드를 활용하는 방식이다. 설계에 많은 시간이 소요되며 처리 속도가 상대적으로 느리다.

배열에서 최댓값을 찾는 로직은 다음과 같다.
```js
const ret = [1, 2, 3, 4, 5, 11, 12]
class List {
  constructor(list) {
    this.list = list
    this.mx = list.reduce((max, num) => num > max ? num : max, 0)
  }
  getMax() {
    return this.mx
  }
}
const a = new List(ret)
console.log(a.getMax())  // 12
```

### 객체지향 프로그래밍의 특징
#### 추상화
복잡한 시스템으로부터 핵심적인 개념 또는 기능을 간추려내는 것을 의미한다.

#### 캡슐화
객체의 속성과 메서드를 마나로 묶고 일부를 외부에 감추어 은닉하는 것을 말한다.

#### 상속성
상위 클래스의 특성을 하위 클래스가 이어받아서 재사용하거나 추가 확장하는 것을 말한다. 코드의 재사용 측면, 계층적인 관계 생성, 유지 보수성 측면에서 중요하다.

#### 다형성
하나의 메서드나 클래스가 다양한 방법으로 동작하는 것을 말한다. 오버로딩과 오버라이딩이 있다.

#### 오버로딩
오버로딩(overloading)은 같은 이름을 가진 메서드를 여러 개 두는 것을 말한다. 메서드의 타입, 매개변수의 유형, 개수 등으로 여러 개를 둘 수 있으며, 컴파일 중에 발생하는 '정적' 다형성이다.
```java
class Person {
  public void eat(String a) {
    System.out.println("I eat " + a);
  }
  
  public void eat(String a, String b) {
    System.out.println("I eat " + a + " and " + b);
}

public class CalculateArea {
  public static void main(String[] args) {
    Person a = new Person();
    a.eat("apple");
    a.eat("tomato", "phodo");
  }
}

/*
I eat apple
I eat tomato and phodo
*/
```

> Python에는 오버로딩이 존재하지 않는다.

#### 오러라이딩
오버라이딩(overriding)은 주로 메서드 오버라이딩을 말하며 상위 클래스로부터 상속받은 메서드를 하위 클래스가 재정의하는 것을 의미한다. 런타인 중에 발생하는 '동적' 다형성이다.
```java
class Animal {
  public void bark() {
    System.out.println("mumu! mumu!");
  }
}

class Dog extends Animal {
  @Override
  public void bark() {
    System.out.println("wal!!! wal!!!");
  }
}

public class Main {
  public static void main(String[] args) {
    Dog d = new Dog();
    d.bark();
  }
}

/*
wal!!! wal!!!
*/
```

### 설계 원칙
객체지향 프로그래밍을 설계할 때는 SOLID 원칙을 지켜야 한다.

#### 단일 책임 원칙
단일 책임 원칙(SRP, Single Responsibility Principle)은 모든 클래스는 각각 하나의 책임만 가져야 하는 원칙이다.

#### 개방-폐쇄 원칙
개방-폐쇄 원칙(OCP, Open Closed Principle)은 확장에는 열려있지만 수정에는 폐쇄적인 원칙이다. 즉, 새로운 기능이나 요구 사항이 추가될 때 기존의 코드를 수정하지 않고도 새로운 기능을 추가할 수 있도록 설계해야 한다.

> 더 많은 기능을 추가하기 위해서는 수정이 아닌 새로운 함수를 추가하는 것이 이상적이다.

#### 리스코프 치환 원칙
리스코프 치환 원칙(LSP, Liskov Substitution Principle)은 하위 클래스는 상위 클래스의 객체로 대체될 수 있어야 한다는 원칙이다. 즉, 하위 클래스는 상위 클래스의 모든 기능을 수행해야 한다.

#### 인터페이스 분리 원칙
인터페이스 분리 원칙(ISP, Interface Segregation Principle)은 하나의 일반적인 인터페이스보다 구체적인 여러 개의 인터페이스를 만들어야 하는 원칙이다.

#### 의존 역전 원칙
의존 역전 원칙(DIP, Dependency Inversion Principle)은 상위 계층은 하위 계층의 변화에 대한 구현으로부터 독립해야 한다는 원칙이다.

***

# 절차형 프로그래밍
절차형 프로그래밍은 로직이 수행되어야 할 연속적인 계산 과정으로 이루어져 있다. 로직이 진행되는 방식으로 코드를 구현하면 되기 때문에 가독성이 좋으며 실행 속도가 빠르다. 단점으로는 모듈화하기 어렵고 유지 보수성이 떨어진다는 점이 있다.

배열에서 최댓값을 찾는 로직은 다음과 같다.
```js
const ret = [1, 2, 3, 4, 5, 11 ,12]
let a = 0
for (let i = 0; i < ret.length; i++) {
  a = Math.max(ret[i], a)
}
console.log(a)  // 12
```