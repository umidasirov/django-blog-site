from django.shortcuts import render , get_object_or_404

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .models import Profile,Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout


def main_view(request):
    return render(request, 'index.html')
@login_required
def users(requset):
    users = User.objects.all()
    context = {'users': users}
    users = User.objects.all()
    return render(requset,'users.html',context)
@login_required
def blog(request):
    blogs = Post.objects.all()
    blogger = {'blog':blogs}
    return render(request,'blogs.html',blogger)
@login_required
def blog_deskripoption(requsest,slug):
    blogs = get_object_or_404(Post,slug=slug)
    return render(requsest,'blog_details.html',{'blogs':blogs})
@login_required
def authors(request, author):
    posts = Post.objects.filter(author__username=author)
    return render(request, 'author.html', {'auth': posts})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # success redirect
        else:
            return render(request, 'login.html', {'error': 'Login yoki parol noto‘g‘ri!'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home');


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        age = request.POST['age']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        job = request.POST['job']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password != password2:
            return render(request, 'register.html', {'error': 'Parollar mos emas!'})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Bu foydalanuvchi allaqachon mavjud!'})

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        Profile.objects.create(user=user, age=int(age), job=job, status="Active")

        login(request, user)
        return redirect('home')

    return render(request, 'register.html')


def test_404(request):
    return render(request, '404.html', status=404)
def profile(request,author):
    posts = Post.objects.filter(author__username=author)
    return render(request,'profile.html',{'auth': posts})
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('profile',author=request.user.username)
@login_required
def new_post(request):
    return render(request,'new_post.html',)
@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if not title or not content:
            return render(request, "new_post.html", {"error": "Iltimos, barcha maydonlarni to'ldiring."})

        Post.objects.create(
            title=title,
            content=content,
            author=request.user
        )
        return redirect("home")
    return render(request, "new_post.html")