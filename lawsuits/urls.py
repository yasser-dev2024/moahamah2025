# lawsuits/urls.py
from django.urls import path
from . import views

app_name = 'lawsuits'

urlpatterns = [
    path('', views.lawsuit_list, name='list'),
    path('create/', views.lawsuit_create, name='create'),
]
