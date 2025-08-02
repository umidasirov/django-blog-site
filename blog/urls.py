from django.contrib import admin
from django.urls import path
from .views import main_view, users,blog,blog_deskripoption,authors,user_login,register,user_logout,profile,delete,new_post,create_post

urlpatterns = [
    path('',main_view,name='home'),
    path('user/',users,name='users'),
    path('blog/',blog,name='blog'),
    path('blog/<slug:slug>/',blog_deskripoption,name='blog_desk'),
    path('user/<str:author>/',authors,name='author'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('profile/<str:author>/', profile, name='profile'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('new_post/', new_post, name='new_post'),
    path('create_post/', create_post, name='create_post'),
]
