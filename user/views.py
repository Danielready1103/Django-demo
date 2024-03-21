from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def user_logout(request):
    logout(request)
    return redirect("login")


def user_profile(request):
    return render(request, "user/profile.html", {"user": request.user})


def user_login(request):
    message = ""

    if request.method == "POST":
        if request.POST.get("register"):
            return redirect("register")
        elif request.POST.get("login"):
            username = request.POST.get("username")
            password = request.POST.get("password")
            if username == "" or password == "":
                message = "帳號或密碼不能為空。"
            else:
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    message = "登入成功。"
                    return redirect("todo")
                else:
                    message = "帳號或密碼錯誤。"

    return render(request, "user/login.html", {"message": message})


def user_register(request):
    message = ""
    form = UserCreationForm()

    # 取得所有使用all OR 取得唯一，使用get OR 篩選功能，使用filter
    # print(User.objects.all())
    # print(User.objects.get(username="Daniel"))
    # print(User.objects.filteret(username="Daniel"))
    try:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            username = request.POST.get("username")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            print(username, password1, password2)

            if len(password1) < 8:
                message = "密碼長度至少8字元"
            elif password1 != password2:
                message = "兩次密碼不匹配"
            else:
                user = User.objects.filter(username=username)
                if len(user) != 0:
                    message = "帳號已經存在。"
                else:
                    User.objects.create_user(
                        username=username, password=password1
                    ).save()
                    message = "註冊成功。"
    except Exception as e:
        print(e)

    return render(request, "user/register.html", {"form": form, "message": message})
