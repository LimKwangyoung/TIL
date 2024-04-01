# 네트워크 기기의 처리 범위
네트워크 기기는 계층별로 처리 범위를 나눌 수 있다. 또한 상위 계층을 처리하는 기기는 하위 계층을 처리할 수 있지만 그 반대는 불가능하다.

- **애플리케이션 계층**: L7 스위치
- **인터넷 계층**: L3 스위치
- **데이터 링크 계층**: L2 스위치, 브리지
- **물리 계층**: NIC, 리피터, AP
***

# 애플리케이션 계층을 처리하는 기기
### L7 스위치
스위치는 여러 장비를 연결하고 데이터 통신을 중재하며 목적지가 연결된 포트로만 전기 신호를 보내 데이터를 전송하는 통신 네트워크 장비이다.
![](https://velog.velcdn.com/images/pyoung/post/a59d503d-e6ac-475c-aaab-dc92d457f28a/image.png)

L7 스위치는 로드밸런서라고도 하며, 서버의 부하를 분산하는 기기이다. 시스템이 처리할 수 있는 트래픽 증가를 목표로 한다.

URL, 서버, 캐시 쿠키들을 기반으로 트래픽을 분산한다. 또한, 바이러스, 불필요한 외부 데이터 등을 걸러내는 필터링 기능 또한 가지고 있으며 응용 프로그램 수준의 트래픽 모니터링도 가능하다.

또한 헬스 체크(health check)를 이용하여 트래픽 분산 대상을 감시한다.

#### L4 스위치와 L7 스위치 차이
로드밸런서로는 L7 스위치 뿐만 아니라 L4 스위치도 있다. L4 스위치는 전송 계층을 처리하는 기기로 IP와 포트를 기반으로 트래픽을 분산한다. 반면 L7 로드밸런서는 IP, 포트 외에도 URL, HTTP, 헤더, 쿠키 등을 기반으로 트래픽을 분산한다.

#### 헬스 체크
로드밸런서는 헬스 체크를 통해 정상적인 서버 또는 비정상적인 서버를 판별하는데, 전송 주기와 재전송 횟수 등을 설정한 이후 반복적으로 서버에 요청을 보낸다.

#### 로드밸런서를 이용한 서버 이중화
로드밸런서의 대표적인 기능으로 서버 이중화가 있다. 로드밸런서는 2대 이상의 서버를 기반으로 가상 IP를 제공하고 이를 기반으로 안정적인 서비스를 제공한다.
![](https://velog.velcdn.com/images/pyoung/post/4b49bda2-b739-4dcb-94ad-f7424ab7c33b/image.png)

***

# 인터넷 계층을 처리하는 기기
### 라우터
라우터(router)는 여러 개의 네트워크를 연결, 분할, 구분시켜주는 역할을 하며다른 네트워크에 존재하는 장치끼리 서로 데이터를 주고받을 때 패킷 소모를 최소화하고 경로를 최적화하여 최소 경로로 패킷을 포워딩한다.

### L3 스위치
L3 스위치란 L2 스위치의 기능과 라우팅 기능을 갖춘 장비를 말한다. 라우터는 소프트웨어 기반의 라우팅과 하드웨어 기반의 라우팅을 하는 것으로 나뉘어지는데, 하드웨어 기반의 라우팅을 담당하는 장치를 L3 스위치라고 한다.

|구분|L2 스위치|L3 스위치|
|:-:|:-:|:-:|
|참조 테이블|MAC 주소 테이블|라우팅 테이블|
|참조 PDU|이더넷 프레임|IP 패킷|
|참조 주소|MAC 주소|IP 주소|
***

# 데이터 링크 계층을 처리하는 기기
### L2 스위치
장치들의 MAC 주소를 MAC 주소 테이블을 통해 관리하며, 연결된 장치로부터 패킷이 왔을 때 패킷 전송을 담당한다.

### 브리지
브리지(bridge)는 두 개의 근거리 통신망(LAN)을 상호 접속할 수 있도록 하는 통신망 연결 장치로, 포트와 포트 사이의 다리 역할을 하며 장치에서 받아온 MAC 주소를 MAC 주소 테이블로 관리한다. 통신망 범위를 확장하고 서로 다른 LAN 등으로 이루어진 하나의 통신망을 구축할 때 쓰인다.
![](https://velog.velcdn.com/images/pyoung/post/0b5f9b6d-c760-470c-a341-399123ba45cd/image.png)

***

# 물리 계층을 처리하는 기기
### NIC
LAN 카드라고 하는 네트워크 인터페이스 카드(NIC)는 2대 이상의 컴퓨터 네트워크를 구성하는 데 사용하며, 네트워크와 빠른 속도로 데이터를 송수신할 수 있도록 컴퓨터 내에 설치하는 확장카드이다.

각 LAN 카드에는 고유의 식별번호인 MAC 주소가 있다.

### 리피터
리피터(repeater)는 약해진 신호 정도를 증폭하여 다른 쪽으로 전달하는 장치이다.
![](https://velog.velcdn.com/images/pyoung/post/c9cc7a4c-3209-4d5f-b9c8-9ab560508770/image.png)

### AP
AP(Access Point)는 패킷을 복사하는 기기이다. AP에 유선 LAN을 연결한 후 다른 장치에서 무선 LAN 기술(와이파이 등)을 사용하여 무선 네트워크 연결을 할 수 있다.