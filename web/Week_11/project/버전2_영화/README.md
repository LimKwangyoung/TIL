# PJT 03

## C. Django 프로젝트
우선 Django 프로젝트를 먼저 구성하였다.

### Django 프로젝트 사전 준비
#### 프로젝트의 이름 : `moviepjt`
```bash
django-admin startproject moviepjt .
```

#### 앱 이름 : `movies`
```bash
python manage.py startapp movies
```

### Django 프로젝트 요구사항
#### 프로젝트의 URLs
```py
# moviepjt/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
]
```

#### `movies` 앱의 URL
```py
# movies/urls.py
from django.contrib import admin
from django.urls import path
from .views import index, community

app_name = 'movies'
urlpatterns = [
    path('', index, name='index'),
    path('community/', community, name='community'),
]
```

#### `movies` 앱의 View
```py
# movies/view.py
from django.shortcuts import render

def index(request):
  return render(request, 'index.html')

def community(request):
  return render(request, 'community.html')
```

#### `base.html`
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{% block title %}{% endblock title %}</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <style>
    {% block style %}{% endblock style %}
  </style>
</head>

<body>
  {% block content %}
  {% endblock content %}
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
    crossorigin="anonymous"></script>
</body>

</html>
```

## A. 메인 페이지
- 제공된 `01-home.html` 활용
  - 편의상 `index.html`로 파일명을 수정
- 영화 목록이 출력되는 메인 페이지
- 상단부터 차례대로 Nav, Header와 Section 세 부분으로 구성

### Nav
1. Bootstrap Navbar Component로 구성
2. 화면을 스크롤 하더라도 항상 화면 상단에 고정
   - `sticky-top`
3. 로고 이미지는 제공된 `logo.png`를 사용
   - `{% static %}` 태그를 사용
4. 내비게이션 메뉴 중 Home, Community는 클릭 시
각각 `01-home.html`, `02-community.html` 로 이동
   - `{% url %}` 태그를 사용
5. 내비게이션 메뉴 중 Login은 클릭 시 Bootstrap Modal Component가 출력
    ```html
    <!-- index.html -->
    <!-- community.html -->
    {% include "nav.html" %}
    {% include "modal.html" %}
    ```
6. Modal Component 내부에는 HTML `form` 태그를 사용
```html
<!-- nav.html -->
{% load static %}

<nav class="navbar navbar-expand-lg bg-body-tertiary sticky-top" data-bs-theme="dark">
  <div class="container-fluid">
    <img src="{% static "images/logo.png" %}" alt="" width="80px" height="40px">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav align-items-end ms-auto">
        <a class="nav-link" aria-current="page" href="{% url "movies:index" %}">Home</a>
        <a class="nav-link" href="{% url "movies:community" %}">Community</a>
        <a class="nav-link" data-bs-toggle="modal" data-bs-target="#exampleModal" href="#">Login</a>
      </div>
    </div>
  </div>
</nav>
```
```html
<!-- modal.html -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Login</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form>
          <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">ID</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
            <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
          </div>
          <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">Password</label>
            <input type="password" class="form-control" id="exampleInputPassword1">
          </div>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Submit</button>
      </div>
    </div>
  </div>
</div>
```

### Header & Section
#### Header
- Bootstrap Carousel Component로 구성
- 이미지는 최소 3장 이상 사용하며 자동으로 재생
```html
<!-- index.html -->
{% load static %}

<header id="carouselExample" class="carousel slide mx-auto">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="{% static "images/header1.jpg" %}" class="d-block w-100" alt="">
      </div>
      <div class="carousel-item">
        <img src="{% static "images/header2.jpg" %}" class="d-block w-100" alt="">
      </div>
      <div class="carousel-item">
        <img src="{% static "images/header1.jpg" %}" class="d-block w-100" alt="">
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </header>
```

#### Section
- 내부의 개별 요소들은 Bootstrap Card Component 로 구성
- 각 Card는 영화 포스터, 제목, 설명을 포함
- Card의 높이는 모두 같으며 각 Card는 서로 좌우 일정한 간격을 가짐
```html
<section class="container">
  <div class="row text-center my-5">
    <h1>Box Office</h1>
  </div>
  <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-5">
    <div class="col">
      <div class="card p-0 h-100">
        <img src="{% static "images/movie1.jpg" %}" class="card-img-top h-100" alt="">
        <div class="card-body px-12">
          <h5 class="card-title">Movie title</h5>
          <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
            content. This content is a little bit longer.</p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card p-0 h-100">
        <img src="{% static "images/movie2.jpg" %}" class="card-img-top h-100" alt="">
        <div class="card-body px-12">
          <h5 class="card-title">Movie title</h5>
          <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
            content. This content is a little bit longer.</p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card p-0 h-100">
        <img src="{% static "images/movie3.jpg" %}" class="card-img-top h-100" alt="">
        <div class="card-body px-12">
          <h5 class="card-title">Movie title</h5>
          <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
            content. This content is a little bit longer.</p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card p-0 h-100">
        <img src="{% static "images/movie4.jpg" %}" class="card-img-top h-100" alt="">
        <div class="card-body px-12">
          <h5 class="card-title">Movie title</h5>
          <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
            content. This content is a little bit longer.</p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card p-0 h-100">
        <img src="{% static "images/movie5.jpg" %}" class="card-img-top h-100" alt="">
        <div class="card-body px-12">
          <h5 class="card-title">Movie title</h5>
          <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
            content. This content is a little bit longer.</p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card p-0 h-100">
        <img src="{% static "images/movie6.jpg" %}" class="card-img-top h-100" alt="">
        <div class="card-body px-12">
          <h5 class="card-title">Movie title</h5>
          <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
            content. This content is a little bit longer.</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

## B. 커뮤니티 페이지
- 제공된 `02-community.html` 활용
  - 편의상 `community.html`로 파일명을 수정
- 게시판이 출력되는 페이지
- Aside, Section과 Pagination 세 부분으로 구성
- 메인 페이지에서 작성한 내비게이션 코드를 그대로 활용

### Aside (게시판 카테고리)
```html
<aside class="col-12 col-lg-2">
  <ul class="list-group">
    <li class="list-group-item">Box Office</li>
    <li class="list-group-item">Movies</li>
    <li class="list-group-item">Genres</li>
    <li class="list-group-item">Actors</li>
  </ul>
</aside>
```

### Section (게시판 카테고리)
```html
<article class="col-12 d-block d-lg-none">
  <hr class='mt-0'>
  <ol class="list-group list-group-flush">
    <li class="list-group-item d-flex justify-content-between align-items-start">
      <div class="ms-2 me-auto">
        <p>Best Movie Ever</p>
        <p>Greate Movie Title</p>
        <p>1 minutes ago</p>
      </div>
      <span class="badge text-bg-light rounded-pill">user</span>
    </li>
    <li class="list-group-item d-flex justify-content-between align-items-start">
      <div class="ms-2 me-auto">
        <p>Movie Test</p>
        <p>Greate Movie TItle</p>
        <p>1 minutes ago</p>
      </div>
      <span class="badge text-bg-light rounded-pill">user</span>
    </li>
    <li class="list-group-item d-flex justify-content-between align-items-start">
      <div class="ms-2 me-auto">
        <p>Movie Ever</p>
        <p>Greate Movie Title</p>
        <p>1 minutes ago</p>
      </div>
      <span class="badge text-bg-light rounded-pill">user</span>
    </li>
  </ol>
</article>

<article class="col-10 d-none d-lg-block">
  <table class="table table-striped">
    <thead>
      <tr>
        <th scope="col">영화 제목</th>
        <th scope="col">글 제목</th>
        <th scope="col">작성자</th>
        <th scope="col">작성 시간</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td scope="row">Great Movie title</td>
        <td>Best Movie Ever</td>
        <td>user</td>
        <td>1 minutes ago</td>
      </tr>
      <tr>
        <td scope="row">Movie Test</td>
        <td>Best Movie Ever</td>
        <td>user</td>
        <td>1 minutes ago</td>
      </tr>
      <tr>
        <td scope="row">Movie Test</td>
        <td>Best Movie Ever</td>
        <td>user</td>
        <td>1 minutes ago</td>
      </tr>
      <tr>
        <td scope="row">Movie Test</td>
        <td>Best Movie Ever</td>
        <td>user</td>
        <td>1 minutes ago</td>
      </tr>
      <tr>
        <td scope="row">Movie Test</td>
        <td>Best Movie Ever</td>
        <td>user</td>
        <td>1 minutes ago</td>
      </tr>
      <tr>
        <td scope="row">Movie Test</td>
        <td>Best Movie Ever</td>
        <td>user</td>
        <td>1 minutes ago</td>
      </tr>
      <tr>
        <td scope="row">Movie Test</td>
        <td>Best Movie Ever</td>
        <td>user</td>
        <td>1 minutes ago</td>
      </tr>
      <tr>
        <td scope="row">Movie Test</td>
        <td>Best Movie Ever</td>
        <td>user</td>
        <td>1 minutes ago</td>
      </tr>
      <tr>
        <td scope="row">Movie Test</td>
        <td>Best Movie Ever</td>
        <td>user</td>
        <td>1 minutes ago</td>
      </tr>
    </tbody>
  </table>
</article>
```

### Pagination
```html
<nav class="d-flex justify-content-center text-align-center">
  <ul class="pagination">
    <li class="page-item">
      <a class="page-link">Previous</a>
    </li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item">
      <a class="page-link" href="#">Next</a>
    </li>
  </ul>
</nav>
```

# 후기
- Django 프로젝트 세팅의 흐름을 숙지하였다.
  - `urls.py` -> `view.py`
- `templates/base.html`의 `block` 태그로는 `<title>`, `<style>`, `<body>` 역할을 하는 것이 유용하다.
- `include` 태그 사용법에 대해 고전하였다.
  - `nav.html`을 사용하는 것은 수월하였다.
  - `modal.html`을 사용하기 위해 modal의 `data-bs-target` 값을 `id`와 연결해보고자 하였다.
  - 그냥 `index.html` 파일과 `community.html`에 `include` 태그를 작성하면 된다.
  - 파일 내에 `include` 태그를 작성하기만 하면 자동으로 `data-bs-target`과 `id`를 연결해주는 강력한 기능이 신기하였다.
- `static` 태그를 reference를 따라 그대로 사용하였다. 이에 관한 정확한 역할이 궁금하다.
- gutters를 사용할 때 `class="col card"`와 같은 형태로 작성하면 x축 방향으로 gutter가 작동하지 않았다. 두 클래스를 구분하여 작성하였는데, 그 이유는 모르겠다.
- 하나하나 `col`에 breakpoint를 작성할 필요 없이 다음과 같이 `row`에 작성하면 편하게 Grid System을 사용할 수 있다.
  ```html
  class="row-cols-1 row-cols-md-2 row-cols-lg-3"
  ```
- Viewport의 Width에 따라 전혀 다른 레이아웃이 나오게끔 하는 기능을 실습 과제를 통해 수월하게 작성하였다.
  - `d-block`과 `d-none`을 적절하게 사용한다면 어렵지 않게 구현할 수 있다.