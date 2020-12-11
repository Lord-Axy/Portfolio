from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.list_projects,name='list_projects'),
    path('code', views.code, name='code'),
]