from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def user_register(requset):
    message = ""
    form = UserCreationForm()
    # print(User.objects.all()) #取得所有
    # print(User.objects.get(usermame="Daniel"))  # 取得唯一
    # print(User.objects.filter(username="Daniel"))  # 取得篩選

    if requset.method == "POST":
        form = UserCreationForm(requset.POST)
        username = requset.POST.get("username")
        password1 = requset.POST.get("password1")
        password2 = requset.POST.get("password2")

        try:
            if len(password1) < 8:
                message = "密碼長度包含至少8個字元"
            elif password1 != password2:
                message = "兩次密碼不匹配"
            else:
                user = User.objects.filter(username=username)
                if len(user) >= 1:
                    message = "帳號已經存在!"
                else:
                    User.objects.create_user(
                        username=username, password=password1
                    ).save()
                    message = "註冊成功。"
        except Exception as e:
            print(e)
            message = "不明錯誤發生。"

    return render(requset, "user/register.html", {"form": form, "message": message})


def user_login(request):
    message = ""
    if request.method == "POST":
        if request.POST.get("register"):
            return redirect("register")
        elif request.POST.get("login"):
            username = request.POST.get("username")
            password = request.POST.get("password")
            if username == "" or password == "":
                message = "帳號或密碼不能為空"
            else:
                # 認證
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    message = "登入成功。"
                    return redirect("profile")
                else:
                    message = "帳號或密碼錯誤。"

    return render(request, "user/login.html", {"message": message})


def user_profile(request):
    return render(request, "user/profile.html", {"user": request.user})


def user_logout(request):
    logout(request)
    return redirect("login")
