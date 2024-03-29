운영체제(OS, Operating System)는 사용자가 컴퓨터를 쉽게 다루게 해주는 인터페이스이다. 참고로 운영체제와 유사하지만 소프트웨어를 추가로 설치할 수 없는 것을 펌웨어(firmware)라고 한다.

# 운영체제의 역할과 구조
### 운영체제의 역할
운영체제의 역할은 다음과 같다.

1. **CPU 스케줄링과 프로세스 관리** : CPU가 소유권을 어떤 프로세스에 할당할지, 프로세스의 생성과 삭제, 자원 할당 및 반환을 관리한다.
2. **메모리 관리** : 한정된 메모리를 어떤 프로세스에 얼만큼 할당해야 하는지 관리한다.
3. **디스크 파일 관리** : 디스크 파일을 어떤 방법으로 보관할지 관리한다.
4. **I/O 디바이스 관리** : I/O 디바이스와 컴퓨터 간에 데이터를 주고받는 것을 관리한다.

> #### 용어
**프로세스** : 컴퓨터에서 실행되고 있는 프로그램

### 운영체제의 구조
![](https://velog.velcdn.com/images/pyoung/post/98d14aca-6ec3-41d0-9fac-6ca75321e33f/image.png)

**GUI** : 사용자가 전자장치와 상호 작용할 수 잇도록 하는 사용자 인터페이스의 한 형태
**드라이버** : 하드웨어를 제어하기 위한 소프트웨어

> GUI와는 다르게 CUI는 그래픽이 아닌 명령어로 처리하는 인터페이스이다. 리눅스 서버는 GUI가 없고 CUI만 있다.

#### 시스템콜
운영체제가 커널에 접근하기 위한 인터페이스이며 유저 프로그램이 운영체제의 서비스를 받기 위해 커널 함수를 호출할 때 사용한다. 유저 프로그램이 I/O 요청으로 트랩(trap)을 발동하면 올바른 요청인지 확인 후 유저 모드가 시스템콜을 통해 커널 모드로 변환되어 실행된다.
![](https://velog.velcdn.com/images/pyoung/post/a5b9dcd9-e8f6-4f86-a710-4db40724de8d/image.png)

이때 유저 모드가 아닌 커널 모드에서 로직을 수행하고, 다시 유저 모드로 돌아가 그 뒤에 있는 유저 프로그램의 로직을 수행한다. 이 과정을 통해 컴퓨터 자원에 대한 직접 접근을 차단할 수 있고 프로그램을 다른 프로그램으로부터 보호할 수 있다.

![](https://velog.velcdn.com/images/pyoung/post/d5800d56-b567-47c1-ad7b-e8fee2396c51/image.png)

프로세스나 스레드에서 운영체제로 요청을 할 때 시스템콜이라는 인터페이스와 커널을 거쳐 운영체제에 전달된다.

> #### 용어
**유저 모드** : 유저가 접근할 수 있는 영역을 제한적으로 둔다. 하드웨어 리소스에 접근 가능하다.
**커널 모드** : 명령, 레지스터, 메모리 제어 등 모든 컴퓨터 자원에 접근할 수 있는 모드이다.
**커널** : 운영체제의 중추적인 역할을 하며 시스템콜 인터페이스를 제공한다.
**스레드** : 프로세스의 실행 가능한 가장 작은 단위

#### modebit
시스템콜이 작동될 때 modebit을 참고해서 유저 모드와 커널 모드를 구분한다. modebit는 1 또는 0을 가지는 플래그 변수로 modebit의 0은 커널 모드, 1은 유저 모드로 설정된다.
![](https://velog.velcdn.com/images/pyoung/post/8a5dbbd3-24be-4cb1-8274-31d812a82fe3/image.png)

# 컴퓨터의 요소
![](https://velog.velcdn.com/images/pyoung/post/be7a3868-e3b6-48a6-9bb3-4342df87fdb8/image.png)

### CPU
CPU는 제어장치, 레지스터, 산술논리연산장치로 구성되어 있다. 인터럽트에 의해 단순히 메모리에 존재하는 명령어를 해석한다.
![](https://velog.velcdn.com/images/pyoung/post/a3ef34d9-b2b2-4104-9d94-15944e4faea2/image.png)

운영체제의 커널이 프로그램을 메모리에 올려 프로세스를 만들면 CPU가 이를 처리한다.

#### 제어장치
프로세스 제작을 지시한다. 입출력장치 간 통신을 제어하고 명령어들을 읽고 해석하며 데이터 처리를 위한 순서를 결정한다.

#### 레지스터
CPU 안에 있는 매우 빠른 임시기억장치를 말한다. CPU와 직접 연결되어 있으므로 연산 속도가 메모리보다 수십 배에서 수백 배까지 빠르다. CPU는 자체적으로 데이터를 저장할 방법이 없기 때문에 레지스터를 거쳐 데이터를 전달한다.

#### 산술논리연산장치
논리 연산을 계산하는 디지털 회로이다.

#### CPU의 연산 처리
![](https://velog.velcdn.com/images/pyoung/post/c337b517-918f-4c61-ba85-0b26c45f52a1/image.png)

#### 인터럽트
어떤 신호가 들어와 처리가 필요한 경우 CPU를 잠시 정지시키는 것을 말한다. 인터럽트가 발생되면 인터럽트 핸들러 함수가 모여 있는 인터럽트 벡터로 가서 인터럽트 함수가 실행된다.

> #### 용어
**인터럽트 핸들러 함수** : 인터럽트가 발생했을 때 이를 핸들링하기 위한 함수이다. 커널 내부의 IRQ를 통해 호출되며 `request_irq()`를 통해 함수를 등록할 수 있다.

**하드웨어 인터럽트**
IO 디바이스에서 발생하는 인터럽트이다. 순차적인 인터럽트 실행을 중지하고 운영체제에 시스템콜을 요청해서 디바이스에 있는 작은 로컬 버퍼에 접근하여 일을 수행한다.

**소프트웨어 인터럽트**
트랩(trap)이라고도 하며, 프로세스가 시스템콜을 호출할 때 발동한다.

### DMA(Direct Memory Access) 컨트롤러
I/O 디바이스가 메모리에 직접 접근할 수 있도록 하는 하드웨어 장치를 말한다. CPU 부하를 막아주며 CPU의 일을 보조한다. 또한 하나의 작업을 CPU와 DMA 컨트롤러가 동시에 하는 것을 방지한다.

### 메모리
전자회로에서 데이터나 상태, 명령어 등을 기록하는 장치를 말하며, 보통 RAM을 일컫는다. 메모리가 클수록 많은 일을 동시에 할 수 있다.

### 타이머
몇 초 안에 작업이 끝나야 한다는 것을 정하고 특정 프로그램에 시간 제한을 다는 역할을 한다. 시간이 많이 걸리는 프로그램이 작동할 때 제한을 걸기 위해 존재한다.

### 디바이스 컨트롤러
컴퓨터와 연결되어 있는 IO 디바이스들의 작은 CPU를 말하며, 옆에 붙어 있는 로컬 버퍼는 데이터를 임시로 저장하기 위한 작은 메모리를 말한다.