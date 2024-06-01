# 파일 내용을 수정 전으로 되돌리기
Modified 파일을 되돌린다. Working Directory에서 파일을 수정했다고 하자. 이 파일의 수정 사항을 취소하고, 원래 모습대로 돌리고자 한다.

### `git restore`
`git restore <file_name>`을 통해 git의 추적이 되고 있는, 즉 버전 관리가 되고 있는 파일만 되돌리기가 가능하다.

1. 이미 버전 관리가 되고 있는 `test.md` 파일을 변경 후 저장한다.
```bash
# test.md

Hello
World <- "World"라는 새로운 내용 추가
--------------------------------
이후 저장
```
2. `test.md`는 `modified` 상태가 되었다.
```bash
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   test.md
        
no changes added to commit (use "git add" and/or "git commit -a")
```
3. `git restore`를 통해 수정 전으로 되돌린다.
```bash
$ git restore test.md
```
```bash
# test.md

Hello
--------------------------------
World가 삭제 되면서, 수정 전으로 되돌아감
```

<span style="color: red;">원래 파일로 덮어썼기 때문에 수정한 내용은 전부 사라진다. 즉 한 번 `git restore`를 통해 수정을 취소하면, 해당 내용을 복원할 수 없다.</span>

***

# 파일 상태를 Unstage로 되돌리기
Staging Area와 Working Directory 사이를 넘나드는 방법이다. `git add`를 통해서 파일을 Staging Area에 올렸다고 하자. 이 파일을 다시 Unstage 상태로 내리고자 한다.

### `git rm --cached`
1. 새 폴더에서 git 초기화 후 진행한다. `test.md` 파일을 생성하고 `git add`를 진행한다.
```bash
$ touch test.md
```
```bash
$ git add test.md
```
```bash
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   test.md
```
2. Staging Area에 올라간 `test.md`를 다시 Unstage 상태로 내린다.
```bash
$ git rm --cached test.md
rm 'test.md'
```
```bash
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        test.md
        
nothing added to commit but untracked files present (use "git add" to track)
```

### `git restore --staged`
1. `test.md` 파일을 커밋한다.
```bash
$ git add .
$ git commit -m 'first commit'
```
2. `test.md`의 내용을 변경하고 `git add`를 진행한다.
```bash
# test.md 파일 변경 후
$ git add test.md
```
```bash
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   test.md
```
3. Staging Area에 올라간 `test.md`를 다시 Unstage 상태로 내린다.
```bash
$ git restore --staged test.md
```
```bash
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   test.md
        
no changes added to commit (use "git add" and/or "git commit -a")
```

> #### 두 명령어의 차이
1. `git rm --cached <file_name>`
	- <span style="color: red;">기존에 커밋이 없는 경우</span>
2. `git restore --staged <file_name>
	- <span style="color: red;">기존에 커밋이 존재하는 경우</span>
    
***

# 바로 직전 완료한 커밋 수정하기
직전 커밋을 취소하고, 모든 파일을 포함해서 다시 커밋 하고자 한다.

### `git commit --amend`
#### 커밋 메세지만 수정하는 경우
1. A 기능을 완성하고 커밋한다.
```bash
$ git commit -m 'B feature completed'
```
2. 현재 커밋 해시 값을 확인한다.
```bash
$ git log
```
3. 커밋 메세지 수정을 위해 다음과 같이 입력한다.
```bash
$ git commit --amend

hint: Waiting for your editor to close the file..[master c01f908] Add no.txt
...
```
4. VIM 편집기가 열리면서 직전 커밋 메세지를 수정할 수 있다.
```bash
B feature completed

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# Date:      Wed Jan 12 01:25:10 2022 +0900
#
# On branch master
#
# Initial commit
#
# Changes to be committed:
#       new file:   test.txt
```
5. 커밋 메세지를 수정하고 저장하면, 새로운 메세지로 변경되며 커밋 <span style="color: red;">해시 값 또한 변경된다.</span>
```bash
$ git log
```

#### 커밋 재작성
1. 실수로 `bar.txt`를 빼고 커밋 했다고 하자.
```bash
$ touch foo.txt bar.txt
$ git add foo.txt
```
```bash
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   foo.txt
        
Untracked files:
  (use "git add <file>..." to include in what will be committed)
bar.txt
```
```bash
$ git commit -m 'foo & bar'

[master 4221af6] foo & bar
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 foo.txt
```
```bash
$ git status

On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        bar.txt
```
2. 누락된 파일을 Staging Area로 이동 시킨다.
```bash
$ git add bar.txt

$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   bar.txt
```
3. `git commit --amend`를 입력한다.
```bash
$ git commit --amend
```
4. VIM 편집기가 열린다.
```bash
foo & bar

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# Date:      Mon Jun 7 22:32:58 2021 +0900
#
# On branch master
# Changes to be committed:
#       new file:   bar.txt
#       new file:   foo.txt
```
5. VIM 편집기를 저장 후 종료하면 직전 커밋이 덮어 씌워진다. 마찬가지로 커밋 <span style="color: red;">해시 값 또한 변경된다.</span>
```bash
$ git commit --amend

[master 7f6c24c] foo & bar
 Date: Mon Jun 7 22:32:58 2021 +0900
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 bar.txt
 create mode 100644 foo.txt
```
6. `git log -p`를 사용하여 직전 커밋의 변경 내용을 확인한다.

> #### `--amend` 장점
- 마지막 커밋 작업에서 뭔가 빠뜨린 것을 넣거나 변경하는 것을 새 커밋으로 분리하지 않고 하나의 커밋에서 처리할 수 있다.
- 추가로 작업한 일이 작다고 하더라도 이전의 커밋을 완전히 새로 고쳐서 새 커밋으로 변경할 수 있다.
- <span style="color: red;">이전의 커밋은 일어나지 않은 일이 되는 것이고, 당연히 히스토리에도 남지 않는다.</span>