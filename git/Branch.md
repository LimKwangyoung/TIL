# Branch
작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 Git의 도구이다. 개발을 하다 보면 코드를 여러 개로 복사해야 하는 일이 자주 생기는데, 코드를 통째로 복사하고 나서 원래 코드와는 상관없이 독립적으로 개발을 진행할 수 있도록 도와준다.
![](https://velog.velcdn.com/images/pyoung/post/e0ee16bb-d9aa-4bf5-8ef9-ba6aa86cdd8b/image.png)


#### 장점
1. 독립 공간을 형성하기 때문에 원본(`master`)에 대해 안전하다.
2. 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능하다.
3. Git의 브랜치는 매우 가벼우며 순식간에 브랜치를 새로 만들고 브랜치 사이를 이동할 수 있다.

#### Branch를 사용해야 하는 이유
1. `master`(`main`)에 대해서 별도의 작업 공간을 만들고, 그 곳에서 되돌리거나 삭제한다.
2. 브랜치는 완전하게 독립이 되어 있어서 어떤 작업을 해도 `master`에는 영향을 끼치지 못한다.

***

# Branch Command
### `git branch`
브랜치 조회, 생성, 삭제 등 브랜치와 관련된 Git 명령어이다.
```bash
# 브랜치 목록 확인
$ git branch

# 원격 저장소의 브랜치 목록 확인
$ git branch -r

# 새로운 브랜치 생성
$ git branch <branch_name>

# 특정 브랜치 삭제
$ git branch -d <branch_name>  # 병합된 브랜치만 삭제 가능
$ git branch -D <branch_name>  # 강제 삭제
```

### `git switch`
현재 브랜치에서 다른 브랜치로 `HEAD`를 이동시키는 명령어이다. `HEAD`는 현재 브랜치를 가리키는 포인터이다.
```bash
# 다른 브랜치로 이동
$ git switch <branch_name>

# 브랜치를 새로 생성과 동시에 이동
$ git switch -c <branch_name>

# 특정 커밋 기준으로 브랜치 생성과 동시에 이동
$ git switch -c <branch_name> <commit Id>
```

#### `git switch` 주의사항
`git switch` 하기 전에, <span style="color: red;">Working Directory 파일이 모두 버전 관리가 되고 있는지</span> 반드시 확인해야 한다.

1. `master` 브랜치와 `feature` 브랜치가 있다고 하자.
2. 만약 `feature` 브랜치에서 `test.txt`를 만들고 `git add` 하지 않은 상태에서 `git switch master`를 하면, `feature` 브랜치에서 만들었던 `test.txt`가 `master` 브랜치에서도 똑같이 생성된다.
3. 이는 Git의 브랜치는 독립적인 작업 공간을 가지지만, 어디까지나 Git이 관리하는 파일 트리에 한하기 때문이다. `git add`를 하지 않은, 즉 Staging Area에 한 번도 올라가지 않은 새 파일은 Git의 버전 관리를 받고 있지 않기 때문에 브랜치가 바뀌더라도 계속 유지된다.
4. 따라서 반드시 `git switch`를 하기 전에는 모든 Working Directory의 파일이 버전 관리가 되고 있는지 확인해야 한다.

***

# Branch Scenario
### 사전 세팅
1. 홈 디렉토리에 `git-branch-practice` 폴더를 생성하고 이동 후 vscode를 실행한다.
```bash
$ mkdir git-branch-practice
$ cd git-branch-practice
$ code .
```
2. Git 저장소를 생성한다.
```bash
$ git init
```
3. `test.txt`를 생성하고 각각 `master-1`, `master-2`, `master-3` 이라는 내용을 순서대로 입력하여 커밋 3개를 작성한다.
```bash
$ touch test.txt

# test.txt에 master-1 작성
$ git add .
$ git commit -m 'master-1'

# test.txt에 master-2 작성
$ git add .
$ git commit -m 'master-2'

# test.txt에 master-3 작성
$ git add .
$ git commit -m 'master-3'
```
4. `git log --oneline`을 입력하면 다음과 같이 나온다.
```bash
$ git log --oneline
0604dcd (HEAD -> master) master-3
9c22c89 master-2
3d71510 master-1
```
![](https://velog.velcdn.com/images/pyoung/post/44c6338e-6bd9-450b-9eb6-94e10b084c61/image.png)

### Branch 생성 및 조회
1. 현재 위치에서 `login` 브랜치를 생성한다.
```bash
$ git branch login
```
2. `login` 브랜치 생성 여부를 확인한다.
```bash
$ git branch
  login
* master
```
> `* master`의 의미는 현재 `HEAD`가 가리키는 브랜치가 `master`라는 뜻이다.

3. `git log --oneline`을 입력하면 다음과 같이 나온다.
```bash
$ git log --oneline
0604dcd (HEAD -> master, login) master-3
9c22c89 master-2
3d71510 master-1
```
> `0604dcd` 커밋 기준으로 `master`와 `login` 브랜치가 위치한 것을 확인할 수 있다.

4. `master` 브랜치에서 1개의 커밋을 추가로 작성한다.
```bash
# test.txt에 master-4 작성
$ git add .
$ git commit -m 'master-4'
```
5. `git log --oneline`을 입력하면 다음과 같이 나온다.
```bash
$ git log --oneline
5ca7701 (HEAD -> master) master-4
0604dcd (login) master-3
9c22c89 master-2
3d71510 master-1
```
![](https://velog.velcdn.com/images/pyoung/post/92a84bb3-5b17-4896-85a0-cd7baf817c2d/image.png)

### Branch 이동
1. 현재 상황에서 `login` 브랜치로 이동한다.
```bash
$ git switch login
```
2. `master` 브랜치의 `test.txt`에 작성한 `master-4`가 지워졌다.
```bash
# login 브랜치의 test.txt 모습

master-1
master-2
master-3
```
3. `git log --oneline`을 입력하면, `HEAD`는 `login` 브랜치를 가리키고 `master` 브랜치가 보이지 않는다.
```bash
$ git log --oneline
0604dcd (HEAD -> login) master-3
9c22c89 master-2
3d71510 master-1
```
4. 브랜치를 조회 해보면 `master` 브랜치가 나온다. 다만 `HEAD`가 `login` 브랜치를 가리키면서 로그도 `login` 브랜치 기준으로 보인 것이다.
```bash
$ git branch
* login
  master
```
5. `git log --oneline --all`을 입력하면 모든 브랜치의 로그를 볼 수 있다.
```bash
$ git log --oneline --all
5ca7701 (master) master-4
0604dcd (HEAD -> login) master-3
9c22c89 master-2
3d71510 master-1
```
![](https://velog.velcdn.com/images/pyoung/post/8c856af6-48e4-4347-b464-6a4b0854d0c4/image.png)

### `login` 브랜치에서 커밋 생성
1. `test.txt` 파일에서 `login-1`이라고 작성한다.
```bash
# login 브랜치의 test.txt 모습

master-1
master-2
master-3
login-1
```
2. 추가적으로 `test_login.txt`도 생성하고 `login-1`이라고 작성한다.
```bash
$ touch test_login.txt

# 이후 test_login.txt에 작성
login-1
```
3. 커밋을 생성한다.
```bash
$ git add .
$ git commit -m 'login-1'
```
4. `git log --oneline --all --graph`를 입력하면, `master` 브랜치와 `login` 브랜치가 다른 갈래로 갈라진 것을 확인할 수 있다.
```bash
$ git log --oneline --graph --all
* 3b0a091 (HEAD -> login) login-1
| * 5ca7701 (master) master-4
|/
* 0604dcd master-3
* 9c22c89 master-2
* 3d71510 master-1
```
![](https://velog.velcdn.com/images/pyoung/post/a9a201d2-168e-40b6-9e79-af6e6accaede/image.png)
