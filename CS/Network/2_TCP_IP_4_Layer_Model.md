인터넷 프로토콜 스위트(Internet Protocol Suite)는 인터넷에서 컴퓨터들이 서로 정보를 주고받는 데 쓰이는 프로토콜의 집합이다. 이를 TCP/IP 4계층 모델로 설명하거나 OSI 7계층 모델로 설명한다.

OSI 7계층은 네트워크의 구조를 7단계로 나눈 것이며, TCP/IP 4계층은 OSI 7계층을 실용성에 기반하여 4단계로 나눈 것이다.
***

# 계층 구조
![](https://velog.velcdn.com/images/pyoung/post/e3acfdfd-a6a9-4419-843b-74b15daea4b8/image.png)

TCP/IP 4계층은 특정 계층이 변경되었을 때 다른 계층이 영향을 받지 않도록 설계되었다.
![](https://velog.velcdn.com/images/pyoung/post/c9c5d606-d6de-402d-b44b-36727d73b757/image.png)

### 애플리케이션 계층
애플리케이션(application) 계층은 FTP, HTTP, SSH, SMTP, DNS 등 응용 프로그램이 사용되는 프로토콜 계층이며, 서비스를 실질적으로 사람들에게 제공하는 층이다.

> #### 용어
**FTP** : 장치와 장치 간의 파일을 전송하는 데 사용되는 표준 통신 프로토콜
**SSH** : 보안되지 않은 네트워크에서 네트워크 서비스를 안전하게 운영하기 위한 암호화 네트워크 프로토콜
**HTTP** : WWW를 위한 데이터 통신의 기초이자 웹 사이트를 이용하는 데 쓰는 프로토콜
**SMTP** : 전자 메일 전송을 위한 인터넷 표준 프로토콜
**DNS** : 도메인 이름과 IP 주소를 매핑해주는 서버.

### 전송 계층
전송(transport) 계층은 송신자와 수신자를 연결하는 통신 서비스를 제공하며, 연결 지향 데이터 스트림 지원, 신뢰성, 흐름 제어를 제공한다. 애플리케이션과 인터넷 계층 사이의 데이터가 전달될 때 중계 역할을 하며, 대표적으로 TCP와 UDP가 있다.

TCP는 패킷 사이의 순서를 보장하고 연결 지향 프로토콜을 사용해서 연결을 하여 신뢰성을 구축해서 수신 여부를 확인하며 '가상회선 패킷 교환 방식'을 사용한다.

UDP는 순서를 보장하지 않고 수신 여부를 확인하지 않으며 단순히 데이터만 주는 '데이터그램 패킷 교환 방식'을 사용한다.

> #### 용어
**연결 지향 프로토콜** : 데이터의 전송 전에 Client와 Server를 연결하는 시스템

#### 가상회선 패킷 교환 방식
각 패킷에는 가상회선 식별자가 포함되며 모든 패킷을 전송하면 가상회선이 해제되고 패킷들은 전송된 '순서대로' 도착하는 방식이다.
![](https://velog.velcdn.com/images/pyoung/post/5cc57880-fa36-4333-8e14-d7c07badf71b/image.png)

#### 데이터그램 패킷 교환 방식
패킷이 독립적으로 이동하며 최적의 경로를 선택한다. 하나의 메세지에서 분할된 여러 패킷은 서로 다른 경로로 전송될 수 있으며 도착한 '순서가 다를 수' 있는 방식이다.
![](https://velog.velcdn.com/images/pyoung/post/9179ebaa-5b09-42a7-a66d-2b83092bc7f7/image.png)

#### TCP 연결 성립 과정
TCP는 신뢰성을 확보할 때 3-way handshake 작업을 진행한다.
![](https://velog.velcdn.com/images/pyoung/post/d6bd58a2-e98e-4e7f-aab2-50e35400ff89/image.png)

1. **SYN 단계** : 클라이언트는 서버에 클라이언트의 ISN을 담아 SYN을 보낸다.
2. **SYN + ACK 단계** : 서버는 클라이언트의 SYN을 수신하고 서버의 ISN을 보내며 승인번호로 클라이언트의 ISN + 1을 보낸다.
3. **ACK 단계** : 클라이언트는 서버의 ISN + 1한 값인 승인번호를 담아 ACK를 서버에 보낸다.

3-way handshaek 이후 신뢰성이 구축되고 데이터 전송을 시작한다. TCP는 해당 과정이 있기 때문에 신뢰성 있는 계층이라 하며 UDP는 해당 과정이 없기 때문에 신뢰성이 없는 계층이라고 한다.

> #### 용어
**SYN** : SYNchronization의 약자로 연결 요청 플래그
**ACK** : ACKnowledgement의 약자로 응답 플래그
**ISN** : Initial Sequence Numbers의 약어로 초기 네트워크 연결을 할 때 할당된 32비트 고유 시퀀스 번호이다. 새로운 TCP 연결의 첫 번째 패킷에 할당된 임의의 시퀀스 번호를 말하며 이는 장치마다 다를 수 있다.

#### TCP 연결 해제 과정
TCP가 연결을 해제할 때는 4-way handshake 작업을 진행한다.
![](https://velog.velcdn.com/images/pyoung/post/f616dcf1-c410-44ae-b8e0-1023e97ae38c/image.png)

1. 클라이언트가 연결을 닫으려고 할 때 FIN으로 설정된 세그먼트를 보낸다. 그리고 클라이언트는 FIN_WAIT_1 상태로 들어가고 서버의 응답을 기다린다.
2. 서버는 클라이언트로 ACK라는 승인 세그먼트를 보낸다. 그리고 CLOSE_WAIT 상태에 들어간다. 클라이언트가 세그먼트를 받으면 FIN_WAIT_2 상태에 들어간다.
3. 서버는 ACK를 보내고 일정 시간 이후 클라이언트에 FIN이라는 세그먼트를 보낸다.
4. 클라이언트는 TIME_WAIT 상태가 되고 다시 서버로 ACK를 보내서 서버는 CLOSED 상태가 된다. 이후 클라이언트는 어느 정도의 시간을 대기한 후 연결이 닫히고 클라이언트와 서버의 모든 자원의 연결이 해제된다.

TIME_WAIT 과정이 있는 이유는 다음과 같다.

1. 지연 패킷이 발생할 경우를 대비하기 위함이다. 패킷이 뒤늦게 도달하고 이를 처리하지 못하면 데이터 무결성 문제가 발생한다.
2. 두 장치가 연결이 닫혔는지 확인하기 위해서이다.

> #### 용어
**TIME_WAIT** : 소켓이 바로 소멸되지 않고 일정 시간 유지되는 상태를 말한다. OS마다 시간이 조금씩 다를 수 있다.
**데이터 무결성** : 데이터의 정확성과 일관성을 유지하고 보증하는 것

### 인터넷 계층
인터넷(internet) 계층은 장치로부터 받은 네트워크 패킷을 IP 주소로 지정된 목적기로 전송하기 위해 사용되는 계층이다. IP, ARP, ICMP 등이 있으며 패킷을 수신해야 할 상대의 주소를 지정하여 데이터를 전달한다. 상대방이 제대로 받았는지에 대해 보장하지 않는 비연결형적인 특징을 지니고 있다.

### 링크 계층
링크 계층은 전선, 광섬유, 무선 등으로 실질적으로 데이터를 전달하며 장치 간에 신호를 주고받는 '규칙'을 정하는 계층이다.

물리 계층과 데이터 링크 계층으로 나뉜다. 물리 계층은 무선 LAN과 유선 LAN을 통해 0과 1로 이루어진 데이터를 보내는 계층을 말하며, 데이터 링크 계층은 '이더넷 프레임'을 통해 에러 확인, 흐름 제어, 접근 제어를 담당한다.

> #### 용어
**이더넷** : LAN 구축을 위해 장치를 연결하는데 널리 사용되는 네트워킹 프로토콜

#### 유선 LAN(IEEE802.3)
유선 LAN을 이루는 이더넷은 IEEE802.3 프로토콜을 따르며 전이중화 통신을 사용한다.

#### 전이중화 통신
전이중화(full duplex) 통신은 양쪽 장치가 동시에 송수신할 수 있는 방식을 말한다. 송신로와 수신로를 나눠서 데이터를 주고 받는다.
![](https://velog.velcdn.com/images/pyoung/post/dbc12a5e-83da-4ad8-bf9e-c1a0cb0da0dd/image.png)

#### CSMA/CD
이전에 유선 LAN은 '반이중화 통신' 중 하나인 CSMA/CD(Carrier Sense Multiple Access with Collision Detection) 방식을 사용했다. 데이터를 보낸 이후 충돌이 발생한다면(Detect) 일정 시간 이후 재전송하는 방식이다. 한 경로를 기반으로 데이터를 보낼 때 충돌에 대해 대비해야 했기 때문이다.

#### 유선 LAN을 이루는 케이블
유선 LAN을 이루는 케이블로는 트위스트 페어 케이블(TP 케이블)과 광섬유 케이블이 있다.

#### 트위스트 페어 케이블
여덟 개의 구리선을 두 개씩 꼬아서 묶은 케이블이다.
![](https://velog.velcdn.com/images/pyoung/post/1a5abc2b-59a8-420c-a0fa-8aa5e8c45c20/image.png)

구리선으로 실드 처리하지 않고 덮은 UTP 케이블과 실드 처리하고 덮은 STP로 나뉜다. 이 LAN 케이블을 꽂을 수 있는 커넥터를 RJ-45 커넥터라고 한다.

#### 광섬유 케이블
레이저를 이용해서 통신하기 때문에 장거리 및 고속 통신이 가능하다. 광섬유 내부와 외부를 다른 밀도를 가지는 섬유로 제작하여, 빛이 내부에서 계속적으로 반사하며 전진한다.
![](https://velog.velcdn.com/images/pyoung/post/2d4cb3fa-5b2d-48fd-bab2-720fed9bb378/image.png)

#### 무선 LAN(IEEE802.11)
무선 LAN 장치는 반이중화 통신을 사용한다.

#### 반이중화 통신
반이중화(half duplex) 통신은 양쪽 장치는 서로 통신할 수 있지만, 동시에는 통신할 수 없으며 한 번에 한 방향만 통신할 수 있다.
![](https://velog.velcdn.com/images/pyoung/post/8321b699-b17b-4524-8819-aa722b0bc589/image.png)

둘 이상의 장치가 동시에 전송하면 충돌이 발생하여 메세지가 손실되거나 왜곡될 수 있기 때문에 충돌 방지 시스템이 필요하다.

#### CSMA/CA
반이중화 통신 중 하나로 데이터를 보내기 전에 일련의 과정을 기반으로 충돌을 방지(Avoid)한다.

#### 무선 LAN을 이루는 주파수
무선 LAN(WLAN)은 무선 신호 전달 방식을 이용하여 2대 이상의 장치를 연결하는 기술이다.

비유도 매체인 공기에 주파수를 쏘아 무선 통신망을 구축하는데, 2.4GHz 대역 또는 5GHz 대역 중 하나를 사용한다. 2.4GHz는 장애물에 강한 특성을 가지고 있지만 전파 간섭이 일어나는 경우가 많고, 5GHz는 상대적으로 깨끗한 전파 환경을 구축할 수 있다.

#### 와이파이
와이파이(wifi)는 전자기기들이 무선 LAN 신호에 연결할 수 있게 하는 기술로, 이를 사용하기 위해서는 무선 접속 장치(AP) 또는 공유기가 있어야 한다. 이는 유선 LAN에 흐르는 신호를 무선 LAN으로 바꾸어준다.

#### BSS
BSS(Basic Service Set)은 기본 서비스 집합으로, 동일 BSS 내에 있는 AP들과 장치들이 서로 통신 가능한 구조를 말한다. 근거리 무선 통신을 제공한다.

#### ESS
ESS(Extended Service Set)은 하나 이상의 연결된 BSS 그룹이다. 장거리 무선 통신을 제공하며 BSS보다 더 많은 가용성과 이동성을 지원한다.
![](https://velog.velcdn.com/images/pyoung/post/505c7bcf-7fd6-410a-972f-c35666eb55cf/image.png)

#### 이더넷 프레임
데이터 링크 계층은 이더넷 프레임을 통해 전달받은 데이터의 에러를 검출하고 캡슐화하며 다음과 같은 구조를 지닌다.
![](https://velog.velcdn.com/images/pyoung/post/a10ccf41-f943-47e0-8449-2e887ad0b59e/image.png)

- **Preamble** : 이더넷 프레임이 시작임을 알린다.
- **SFD(Start Frame Delimiter)** : 다음 바이트로부터 MAC 주소 필드가 시작됨을 알린다.
- **DMAC, SMAC** : 수신, 송신 MAC 주소
- **Ether Type** : 데이터 계층 위의 계층인 IP 프로토콜을 정의한다.
- **Payload** : 전달받은 데이터
- **CRC** : 에러 확인 비트

> #### 용어
**MAC 주소** : 각 장치에는 네트워크를 연결하기 위한 LAN 카드가 있는데, 이를 구별하기 위한 식별변호이다.

### 계층 간 데이터 송수신 과정
![](https://velog.velcdn.com/images/pyoung/post/f110d377-a69e-4dc0-a947-f4565a3a46d9/image.png)

애플리케이션 게층에서 전송 계층으로 요청(request) 값들이 캡슐화 과정을 거쳐 전달되고, 다시 링크 계층을 통해 해당 서버와 통신하고, 해당 서버의 링크 계층으로부터 애플리케이션까지 비캡슐화 과정을 거쳐 데이터가 전송된다.

#### 캡슐화 과정
캡슐화 과정은 상위 계층의 헤더와 데이터를 하위 계층의 데이터 부분에 포함시키고 해당 계층의 헤더를 삽입하는 과정이다.
![](https://velog.velcdn.com/images/pyoung/post/ef494c77-051c-462d-8d51-69705598e38c/image.png)

애플리케이션 계층의 데이터가 전송 계층으로 전달되면서 '세그먼트' 또는 '데이터그램'화되며 TCP(L4) 헤더가 붙여진다. 이후 인터넷 계층으로 가면서 IP(L3) 헤더가 붙여지게 되며 '패킷'화가 되고, 이후 링크 게층으로 전달되면서 프레임 헤더와 프레임 트레일러가 붙어 '프레임'화가 된다.

#### 비캡슐화 과정
비캡슐화 과정은 하위 계층에서 상위 계층으로 가며 각 계층의 헤더 부분을 제거하는 과정을 말한다.
![](https://velog.velcdn.com/images/pyoung/post/9cf878ae-cb35-4f9c-8159-21de35ff3734/image.png)

프레임화된 데이터는 다시 패킷화를 거쳐 세그먼트, 데이터그램화를 거쳐 메세지화가 된다.
***

# PDU
PDU(Protocol Data Unit)은 네트워크의 어떠한 계층에서 계층으로 데이터가 전달될 때 한 덩어리의 단위를 말한다.

PDU는 제어 관련 정보들이 포함된 '헤더'와 데이터를 의미하는 '페이로드'로 구성되어 있으며 계층마다 부르는 명칭이 다르다.

- **애플리케이션 계층** : 메세지
- **전송 계층** : 세그먼트(TCP), 데이터그램(UDP)
- **인터넷 계층** : 패킷
- **링크 계층** : 프레임(데이터 링크 계층), 비트(물리 계층)

예를 들어 애플리케이션 계층은 '메세지'를 기반으로 데이터를 전달하는데, HTTP의 헤더가 문자열인 것을 볼 수 있다. `curl` 명령어를 이용하여 PDU 테스팅을 해볼 수 있다.

참고로 PDU 중 아래 계층인 비트로 송수힌 하는 것이 가장 빠르고 효율성이 높다. 하지만 애플리케이션 계층에서는 문자열 기반으로 송수신하는데, 다른 값들을 넣는 확장이 쉽기 때문이다.