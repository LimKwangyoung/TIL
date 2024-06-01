# Branch Merge
### `git merge`
분기된 브랜치를 하나로 병합한다. `git merge <branch_name>` 명령어를 통해 병합하며, <span style="color: red;">병합하기 전에 일단 다른 브랜치를 합치려고 하는, 즉 메인 브랜치로 `switch` 해야한다.</span>
```bash
# 1. 현재 branch1과 branch2가 있고, HEAD가 가리키는 곳은 branch1 이다.
$ git branch
* branch1
  branch2

# 2. branch2를 branch1에 합치려면?
$ git merge branch2

# 3. branch1을 branch2에 합치려면?
$ git switch branch2
$ git merge branch1
```

### Merge 종류
#### Fast-Forward
브랜치를 병합할 때 마치 빨리감기처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 것이다. 병합 과정 없이 단순히 브랜치의 포인터가 이동한다.

1. 현재 `master`는 `C2` 커밋을, `hotfix`는 `C4` 커밋을 가리키고 있다.
![](https://velog.velcdn.com/images/pyoung/post/867f147a-d969-429e-8a3a-a13efea2c491/image.png)
2. `master`에 `hotfix`를 병합한다.
```bash
$ git switch master
$ git merge hotfix
Updating s1d5f1s..1325sd4
Fast-forward
 index.html | 2 ++
 1 file changed, 2 insertions(+)
```
3. `hotfix`가 가리키는 `C4`는 `C2`에 기반한 커밋이므로, `master`가 `C4`에 이동하게 된다.
![](https://velog.velcdn.com/images/pyoung/post/b3afb163-cd56-4d97-9e8a-64f0a6290001/image.png)

이렇게 따로 병합 과정 없이 브랜치의 포인터가 이동하는 것을 `Fast-Forward`라고 한다.

#### 3-Way Merge (Merge commit)
브랜치를 병합할 때 각 브랜치의 커밋 두 개와 공통 조상 하나를 사용하여 병합하는 것이다. 두 브랜치에서 다른 파일 혹인 같은 파일의 다른 부분을 수정했을 때 가능하다.

1. 현재 `master`는 `C4` 커밋을, `iss53`은 `C5` 커밋을 가리키고 있다. `master`와 `iss53`의 공통 조상은 `C2` 커밋이다.
![](https://velog.velcdn.com/images/pyoung/post/f548929a-5d08-4f99-ac83-f4bee2cf6c3a/image.png)
2. `master`에 `iss53`을 병합한다.
```bash
$ git switch master
Switched to branch 'master'

$ git merge iss53
Merge made by the 'ort' strategy.
index.html |    1 +
1 file changed, 1 insertion(+)
```
3. `master`와 `iss53`은 갈래가 나누어져 있기 때문에 Fast-Forward로 합쳐질 수 없다. 따라서 공통 조상인 `C2`와 각자가 가리키는 커밋인 `C4`, `C5`를 비교하여 `3-way merge`를 진행한다.
![](https://velog.velcdn.com/images/pyoung/post/9848219e-ffff-4605-b169-e23fb40e3099/image.png)
4. 이때 생긴 `C6`는 `master`와 `iss53`이 병합되면서 발생한 Merge Commit이다.

#### Merge Conflict
병합하는 두 브랜치에서 같은 파일의 다른 부분을 수정한 경우, Git이 어느 브랜치의 내용으로 작성해야 하는지 판단하지 못해 발생하는 충돌 현상을 말한다. 결국은 사용자가 직접 내용을 선택해서 Conflict를 해결해야 한다.

1. 현재 `master`는 `C4` 커밋을, `iss53`은 `C5` 커밋을 가리키고 있다. `master`와 `iss53`의 공통 조상은 `C2` 커밋이다.
![](https://velog.velcdn.com/images/pyoung/post/f548929a-5d08-4f99-ac83-f4bee2cf6c3a/image.png)
2. `master`와 `iss53`이 같은 파일의 같은 부분을 수정하고 병합한다.
```bash
$ git merge iss53
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```
3. `git status`로 충돌이 일어난 파일을 확인한다.
```bash
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
Unmerged paths:
  (use "git add <file>..." to mark resolution)
    both modified:      index.html
no changes added to commit (use "git add" and/or "git commit -a")
```
4. `index.html`을 열어보면 아래와 같이 충돌 내용이 나온다.
```html
<<<<<<< HEAD:index.html
<div id="footer">contact : email.support@github.com</div>
=======
<div id="footer">
 please contact us at support@github.com
</div>
>>>>>>> iss53:index.html
```
5. 이 중 하나를 선택할 수도 있고, 둘 다 선택할 수도 있고, 아예 새롭게 작성할 수도 있다.
```html
<div id="footer">
please contact us at email.support@github.com
</div>
```
6. 이후 `git add`와 `git commit`을 통해 병합한 내용을 커밋할 수 있다.
```bash
$ git add .
$ git commit
```
7. Vim 편집기가 켜지며 이를 이용해서 커밋 내역을 수정할 수 있다. 수정을 마치거나 수정할 것이 더이상 없을 경우 `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료한다.
```bash
Merge branch 'iss53'

Conflicts:
    index.html
#
# It looks like you may be committing a merge.
# If this is not correct, please remove the file
#   .git/MERGE_HEAD
# and try again.

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# All conflicts fixed but you are still merging.
#
# Changes to be committed:
#   modified:   index.html
#
```

***

# Branch Merge Scenario
### 사전 세팅
```bash
$ mkdir git_merge
$ cd git_merge

$ git init
$ touch test.txt

# test.txt 에 master test 1 을 입력 후 저장

$ git status
$ git add .

$ git commit -m 'master test 1'
```

### 3가지 Merge 상황
#### fast-forward
`login` 브랜치가 생성된 이후 `master` 브랜치에 변경 사항이 없는 상황이다. 즉, `master` 브랜치에서 `login` 브랜치를 병합할 때 `login` 브랜치가 `master` 브랜치 이후의 커밋을 가리키고 있으면 그저 `master` 브랜치가 `login` 브랜치와 동일한 커밋을 가리키도록 이동시킬 뿐이다.
![](https://velog.velcdn.com/images/pyoung/post/ca15af2b-caea-4d0c-8200-26a4b8254a43/image.png)

1. `login` 브랜치 생성 및 이동한다.
```bash
$ git switch -c login
```
2. 특정 작업 완료 후 커밋한다.
```bash
$ touch login.txt
$ git add .
$ git commit -m 'login test 1'
```
3. `master` 브랜치로 이동한다.
```bash
$ git switch master

$ git log --oneline --all --graph
* df231d0 (login) login test 1
* 1e62b4c (HEAD -> master) master test 1
```
4. `master`에 병합 `login`을 병합한다.
```bash
$ git merge login
Updating 43fab3e..2fe539c
Fast-forward
 login.txt | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 login.txt
```
5. fast-forward로 단순히 `HEAD`를 앞으로 빨리감기 하였다.
```bash
$ git log --oneline --all --graph
* 2fe539c (HEAD -> master, login) login test 1
* 43fab3e master test 1
```

#### 3-Way Merge (Merge Commit)
현재 브랜치(`master`)가 가리키는 커밋이 병합할 브랜치의 조상이 아니면, git은 각 브랜치가 가리키는 커밋 2개와 공통조상 하나를 사용하여 3-Way Merge 한다.

단순히 브랜치 포인터를 최신 커밋으로 옮기는 게 아니라 3-Way Merge의 결과를 별도의 커밋으로 만들고 나서 해당 브랜치가 그 커밋을 가리키도록 이동시킨다.
![](https://velog.velcdn.com/images/pyoung/post/18798d7c-ee66-4403-ae70-675a7a64a4d4/image.png)

1. `signout` 브랜치 생성 및 이동한다.
```bash
$ git switch -c signout
```
2. 특정 작업 완료 후 커밋한다.
```bash
$ touch signout.txt

$ git add .
$ git commit -m "signout test 1"
[signout d9f33e2] signout test 1
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 signout.txt
 
$ git log --oneline --all --graph
* d9f33e2 (HEAD -> signout) signout test 1
* 2fe539c (master) login test 1
* 43fab3e master test 1
```
3. `master` 브랜치로 이동한다.
```bash
$ git switch master
```
4. `master`에 추가 작업 후 커밋한다. 단, <span style="color: red;">`signout` 브랜치와 다른 파일</span>을 생성 혹은 수정한다.
```bash
$ touch master.txt

$ git add .
$ git commit -m "master test 2"

$ git log --oneline --all --graph
* 07fae72 (HEAD -> master) master test 2
| * d9f33e2 (signout) signout test 1
|/
* 2fe539c login test 1
* 43fab3e master test 1
```
5. `master`에 `signout`을 병합한다. 자동 merge commit이 발생한다.
```bash
$ git merge signout
Merge made by the 'recursive' strategy.
 signout.txt | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 signout.txt
```
6. 로그를 확인해보면 다음과 같다.
```bash
$ git log --oneline --all --graph
*   1170a02 (HEAD -> master) Merge branch 'signout'
|\
| * d9f33e2 (signout) signout test 1
* | 07fae72 master test 2
|/
* 2fe539c login test 1
* 43fab3e master test 1
```

#### Merge Conflict
병합하는 두 브랜치에서 <span style="color: red;">같은 파일의 같은 부분을 동시에 수정</span>하고 병합하면 Git은 해당 부분을 자동으로 병합하지 못하고 충돌이 일어난다.

<span style="color: red;">반면 동일 파일이더라도 서로 다른 부분을 수정했다면, Conflict 없이 자동으로 Merge Commit 된다.</span>
![](https://velog.velcdn.com/images/pyoung/post/cb7bfa12-a9f3-40de-a3e6-78ad6fb10cf0/image.png)

1. `hotfix` 브랜치 생성 및 이동한다.
```bash
$ git switch -c hotfix
```
2. 특정 작업 완료 후 커밋한다.
```bash
# test.txt 수정

master test 1
이건 hotfix 에서 작성한 문장이에요!!
```
```bash
$ git add .

$ git commit -m 'hotfix test 1'
[hotfix e6cf5ec] hotfix test 1
 1 file changed, 2 insertions(+)
 
$ git log --graph --oneline --all
* e6cf5ec (HEAD -> hotfix) hotfix test 1
*   1170a02 (master) Merge branch 'signout'
|\
| * d9f33e2 signout test 1
* | 07fae72 master test 2
|/
* 2fe539c login test 1
* 43fab3e master test 1
```
3. `master` 브랜치로 이동한다.
```bash
$ git switch master
```
4. 특정 작업(`hotfix`와 동일 파일의 동일 부분 수정) 완료 후 커밋한다.
```bash
# test.txt 수정

master test 1
이건 master 에서 작성한 코드에용ㅎㅎ!!
```
```bash
$ git add .
$ git commit -m "master test 3"
$ git log --oneline --all --graph
* 1bc2eeb (HEAD -> master) master test 3
| * e6cf5ec (hotfix) hotfix test 1
|/
*   1170a02 Merge branch 'signout'
|\
| * d9f33e2 signout test 1
* | 07fae72 master test 2
|/
* 2fe539c login test 1
* 43fab3e master test 1
```
5. `master`에 `hotfix`를 병합한다.
```bash
$ git merge hotfix
```
6. 같은 파일의 같은 문장을 수정했기 때문에 Merge Conflict가 발생한다.
![](https://velog.velcdn.com/images/pyoung/post/e37d18c3-e14c-4d2f-af3e-728c063eb253/image.png)
7. Merge Conflict가 일어났을 때 Git이 어떤 파일을 Merge 할 수 없었는지 살펴보려면 `git status` 명령을 이용한다.
```bash
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)
  
Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   test.txt
        
no changes added to commit (use "git add" and/or "git commit -a")
```
8. 충돌을 해결하려면 위쪽이나 아래쪽 내용 중에서 고르거나 새로 작성하여 병합해야 한다. 즉 `<<<<<<<`, `=======`, `>>>>>>>` 가 포함된 행을 삭제한다.
![](https://velog.velcdn.com/images/pyoung/post/f9754586-2af0-4bb5-8c27-e3f3d3de4b5f/image.png)
9. Merge Commit을 진행한다. Vim 에디터가 등장한다. 자동으로 작성된 커밋 메세지를 확인하고 `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료한다.
```bash
$ git add .
$ git commit
```
![](https://velog.velcdn.com/images/pyoung/post/2070b9cb-c5c8-4b63-9c32-44b257c0a6fb/image.png)
10. 로그를 확인해보면 다음과 같다.
```bash
$ git log --oneline --all --graph
*   eec8da4 (HEAD -> master) Merge branch 'hotfix'
|\
| * e6cf5ec (hotfix) hotfix test 1
* | 1bc2eeb master test 3
|/
*   1170a02 Merge branch 'signout'
|\
| * d9f33e2 signout test 1
* | 07fae72 master test 2
|/
* 2fe539c login test 1
* 43fab3e master test 1
```