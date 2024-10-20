from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    messages.info(request, "Welcome to")
    messages.error(request, "Welcome to")
    return render(request, "home.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "Пользователь не существует")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Вы успешно авторизовались")
            return redirect("home")
        else:
            messages.error(request, "Неверный логин или пароль")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Вы вышли из системы")
    return redirect("home")
