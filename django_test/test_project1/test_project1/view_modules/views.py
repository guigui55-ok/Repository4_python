
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import requests 


def hello_jango(request):
    print('views.py > index')
    return HttpResponse("Hello, Django!")

def test_index(request):
    print('views.py > index')
    return render(request, 'test_index.html')

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('members')  # メンバー専用ページへ
        else:
            messages.error(request, 'ログイン失敗：ユーザー名またはパスワードが間違っています。')
            return render(request, 'login.html', {'error': 'ログイン失敗：ユーザー名またはパスワードが間違っています。'})
    return render(request, 'login.html')

def signin_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('members')  # サインイン後、メンバー専用ページへ
    else:
        form = UserCreationForm()
    return render(request, 'signin.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')  # ログインページにリダイレクト

def members_view(request):
    return redirect('members')  # ログインページにリダイレクト