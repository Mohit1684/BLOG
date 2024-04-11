from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from django.contrib.auth.models import User, auth

def index(request):
    posts=Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    posts=Post.objects.get(id=pk)
    return render(request, 'post.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            else:
                user= User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('admin/')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')

    else:
        return render(request, 'register.html')