from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Keyword, Trend
from .forms import KeywordForm

from bs4 import BeautifulSoup
from selenium import webdriver
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# Create your views here.
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


@require_http_methods(['POST'])
def keyword_detail(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')


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


@require_http_methods(['GET'])
def crawling_histogram(request):
    context = {
        'bar_image': f'data:image/png;base64,{draw()}',
    }
    return render(request, 'trends/crawling_histogram.html', context)


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