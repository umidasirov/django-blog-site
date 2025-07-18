from django.contrib import admin
from django.urls import path
from .views import main_view, users,blog

urlpatterns = [
    path('',main_view,name='home'),
    path('user/',users,name='users'),
    path('blog/',blog,name='blog')
]
