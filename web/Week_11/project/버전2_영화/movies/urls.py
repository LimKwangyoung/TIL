from django.contrib import admin
from django.urls import path
from .views import index, community

app_name = 'movies'
urlpatterns = [
    path('', index, name='index'),
    path('community/', community, name='community'),
]
