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