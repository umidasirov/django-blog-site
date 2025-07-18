from django.shortcuts import render
from .models import Profile,Post
from django.contrib.auth.models import User

def main_view(request):
    return render(request, 'index.html')
def users(requset):
    users = User.objects.all()
    context = {'users': users}
    users = User.objects.all()
    return render(requset,'users.html',context)
def blog(request):
    blogs = Post.objects.all()
    blogger = {'blog':blogs}
    return render(request,'blogs.html',blogger)
