# PJT 04 - 버전2 영화

## A. 프로젝트와 앱, 모델, 폼 생성
### 프로젝트 생성
```bash
$ django-admin startproject mypjt .
```
### 앱 생성
```bash
$ python manage.py startapp movies
$ python manage.py startapp accounts
```
### 모델 클래스
```py
# movies/models.py

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField()
```
```py
# accounts/models.py

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

### 폼 클래스
```py
# movies/forms.py

from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
```
```py
# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'username')
```

## B. `movies` 앱의 View 함수
### 허용 HTTP Method
View 함수에 공통적으로 HTTP Method를 적용하기 위해 데코레이터를 사용하였다.
```py
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
@require_http_methods(['GET', 'POST'])
```

### URL
다음의 URL을 기준으로 View 함수를 작성하였다. View 함수의 코드는 길기 때문에 작성을 생략하겠다.
```py
# movies/urls.py

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
]
```

## C. `accounts` 앱의 View 함수
### 허용 HTTP Method
View 함수에 공통적으로 HTTP Method를 적용하기 위해 데코레이터를 사용하였다.
```py
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
@require_http_methods(['GET', 'POST'])
```

### URL
다음의 URL을 기준으로 View 함수를 작성하였다. View 함수의 코드는 길기 때문에 작성을 생략하겠다.
```py
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]
```
비밀번호 변경 URL은 프로젝트 디렉토리의 URL에서 작성하였다.
```py
# mypjt/urls.py

from django.urls import path
from accounts import views

urlpatterns = [
    ...,
    path('<int:user_pk>/password/', views.change_password, name='change_password'),
]
```

## D. 댓글 작성 기능
`movies/detail.html` 파일에 댓글 작성 기능을 추가하였다. `Comment` 모델은 `User` 클래스와 `Movie` 클래스와 관련하여 외래 키 필드 `user`와 `movie`를 갖는다.
```py
# movies/models.py

from django.db import models
from django.conf import settings

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
```
또한 ModelForm인 `CommentForm`을 만는다.
```py
# movies/forms.py

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
```
다음의 URL을 기준으로 댓글 생성 View 함수를 작성하였다. View 함수의 코드는 길기 때문에 작성을 생략하겠다.
```py
# moveis/urls.py

from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    ...,
    path('<int:movie_pk>/create_comment/', views.create_comment, name='create_comment'),
    path('<int:movie_pk>/delete/<int:comment_pk>', views.delete_comment, name='delete_comment'),
]
```

## E. Issue
### 로그아웃 버튼
Navbar의 로그아웃 버튼을 CSS로 디자인하는데 있어서 어려움을 겪었다. 로그아웃 기능은 `<form>` 태그를 이용하기 때문에 `submit` 버튼이 정해져있다.  
하지만 예시에는 버튼이 아닌 `<a>` 태그의 형태이다. 로그아웃 기능은 POST 요청을 보내야 하기 때문에 `<a>` 태그의 형태로 POST 요청을 어떻게 보내야 할지에 대해 고민하였다.  
`<form>` 태그 내에 `<a>` 태그를 작성하되 JavaScript을 이용하여 다음과 같이 해결하였다.
```html
<!-- templates/base.html -->

<form action="{% url 'accounts:logout' %}" method="POST">
  {% csrf_token %}
  <input type="hidden">
  <a href="#" class="nav-link" onclick="this.parentNode.submit()">로그아웃</a>
</form>
```
`<input>` 태그를 `hidden` 속성으로 숨기고 `<a>` 태그에서 `onclick` 이벤트가 발생하였을 때 부모 태그의 `type` 속성을 `submit`으로 변경하여 POST 요청을 하였다.

### 언어
렌더링 된 페이지의 언어가 영어로 되어있다. 예시에는 한글로 되어있기 때문에 프로젝트의 `settings.py`에서 언어를 설정하였다.
```py
# mypjt/settings.py

LANGUAGE_CODE = 'ko-kr'
```

### 회원정보수정
회원정보수정 페이지로 들어가면 다음과 같은 문구가 뜬다.
```txt
비밀번호:

비밀번호가 설정되지 않습니다.
원본 비밀번호는 저장되지 않으므로, 해당 사용자의 비밀번호를 확인할 수 없습니다. 다만 이 폼을 사용하여 비밀번호를 변경할 수 있습니다.
```
예시에는 보이지 않기 때문에 `<style>` 태그를 사용하여 `display: none;`을 설정하였다.
```html
<!-- update.html -->

{% block style %}
    #id_password, .helptext, form>p:nth-child(6) {
        display: none;
    }
{% endblock style %}
```

# 후기
- MVT 모델의 전반적인 기능을 처음부터 끝까지 모두 작성할 수 있어서 개념 정리에 많은 도움이 되었습니다.
- 로그인, 로그아웃, 회원가입 기능에 숙지가 더 필요할 것 같습니다.
- JavaScript를 활용해야 더 많은 기능을 구현할 수 있을 것 같습니다.
- CSS와 같이 구현하는 것에 어려움을 많이 겪었습니다.