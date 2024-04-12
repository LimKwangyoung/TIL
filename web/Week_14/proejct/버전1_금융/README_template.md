# PJT 05 - 버전 2 금융

## A. 공통 요구 사항
Django 프로젝트의 이름은 `mypjt`, 앱 이름은 `trends`로 한다.
```bash
$ django-admin startproject mypjt .
$ python manage.py startapp trends
```

## B. Model
`Keyword`, `Trend` 모델 클래스를 정의한다. `Trend` 클래스의 `name` 필드를 외래 키로 사용한다.
```py
# models.py

from django.db import models

class Keyword(models.Model):
    name = models.CharField(max_length=10)
    created_at = models.DateField(auto_now_add=True)

class Trend(models.Model):
    name = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    result = models.IntegerField()
    search_period = models.TextField()
    created_at = models.DateField(auto_now_add=True)
```

## C. URL
```py
# urls.py

from django.urls import path
from . import views

app_name = 'trends'
urlpatterns = [
    path('keyword/', views.keyword, name='keyword'),
    path('keyword/<int:pk>/', views.keyword_detail, name='keyword_detail'),
    path('keyword/crawling/', views.crawling, name='crawling'),
    path('keyword/crawling/histogram/', views.crawling_histogram, name='crawling_histogram'),
    path('keyword/crawling/advanced/', views.crawling_advanced, name='crawling_advanced'),
]
```

## D. View
### `keyword`
ModelForm인 `KeywordForm`을 정의하고 keyword를 ModelForm에 저장한다.
```py
# views.py

from .forms import KeywordForm

@require_http_methods(['GET', 'POST'])
def keyword(request):
    keywords = Keyword.objects.all()
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trends:keyword')
    else:
        form = KeywordForm()
    context = {
        'keywords': keywords,
        'form': form,
    }
    return render(request, 'trends/keyword.html', context)
```

### `keyword_detail`
```py
# views.py

@require_http_methods(['POST'])
def keyword_detail(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')
```

### `crawling`
crawling을 위한 함수 `get_data`를 정의한다. `search_period`의 값에 따라 crawling하는 url이 다르므로, 이를 파라미터 `option`으로 분기한다.
```py
# views.py

def get_data(keyword, option=False):
    if not option:
        url = f'https://www.google.com/search?q={keyword}'
    else:
        url = f'https://www.google.com/search?q={keyword}&tbs=qdr:y'

    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    string = soup.select_one('div#result-stats').text
    start = end = 7
    for i in range(len(string) - 1, -1, -1):
        if string[i] == '개':
            end = i
            break
    return int("".join(string[start:end].split(',')))
```
키워드가 이미 저장되어 있다면 `result`를 변경하고, 그렇지 않다면 새로 생성한다.
```py
# views.py

@require_http_methods(['GET'])
def crawling(request):
    keywords = Keyword.objects.all()
    trends = Trend.objects.filter(search_period='all')
    for keyword in keywords:
        num = get_data(keyword.name)
        trend = Trend.objects.filter(search_period='all', name=keyword)
        if trend:
            trend.result = num
        else:
            trend = Trend(result=num, search_period='all', name=keyword)
            trend.save()
    
    context = {
        'trends': trends,
    }
    return render(request, 'trends/crawling.html', context)
```

### `crawling_histogram`
그래프를 생성해주는 `draw` 함수를 정의한다. `draw` 함수는 `search_period` 값에 따라 사용하는 데이터가 다르다.
```py
# views.py

def draw(option=False):
    if not option:
        trends = Trend.objects.filter(search_period='all')
    else:
        trends = Trend.objects.filter(search_period='year')

    plt.clf()
    x_values, y_values = [], []
    for trend in trends:
        x_values.append(trend.name.name)
        y_values.append(trend.result)

    plt.bar(x_values, y_values)
    plt.title('Technology Trend Analysis')
    plt.xticks(rotation=45)
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.grid(True)
    plt.legend(labels=['Trends'])

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    return image_base64
```
```py
# views.py

@require_http_methods(['GET'])
def crawling_histogram(request):
    context = {
        'bar_image': f'data:image/png;base64,{draw()}',
    }
    return render(request, 'trends/crawling_histogram.html', context)
```

### `crawling_advanced`
`search_period='year'`일 경우를 생각하여 함수를 작성한다. 마찬가지로 키워드가 이미 저장되어 있다면 `result`를 변경하고, 그렇지 않다면 새로 생성한다.
```py
# views.py

@require_http_methods(['GET'])
def crawling_advanced(request):
    keywords = Keyword.objects.all()
    for keyword in keywords:
        num = get_data(keyword.name, option=True)
        trend = Trend.objects.filter(search_period='year', name=keyword)
        if trend:
            trend.result = num
        else:
            trend = Trend(result=num, search_period='year', name=keyword)
            trend.save()
    context = {
        'bar_image': f'data:image/png;base64,{draw(option=True)}',
    }
    return render(request, 'trends/crawling_advanced.html', context)
```

# 후기
- 처음 제대로 해보는 웹 크롤링을 숙지하는데 있어서 약간의 어려움이 있었다.
- 키워드가 이미 저장되어 있을 경우를 작성하는 것이 헷갈렸다.
- 같은 기능을 담당하는 함수들을 따로 작성하는 것이 더 효율적이다.