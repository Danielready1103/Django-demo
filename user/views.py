from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.


def user_register(requset):
    message = ""
    form = UserCreationForm()
    # print(User.objects.all()) #取得所有
    # print(User.objects.get(usermame="Daniel"))  # 取得唯一
    print(User.objects.filter(username="Daniel"))  # 取得篩選

    if requset.method == "POST":
        form = UserCreationForm(requset.POST)
        username = requset.POST.get("username")
        password1 = requset.POST.get("password1")
        password2 = requset.POST.get("password2")

        if len(password1) < 8:
            message = "密碼長度包含至少8個字元"
        elif password1 != password2:
            message = "兩次密碼不匹配"
        else:
            user = User.objects.filter(username=username)
            if len(user) >= 1:
                message = "帳號已經存在!"
            else:
                User.objects.create_user(username=username, password=password1).save()
                message = "註冊成功。"

        print(username, password1, password2)

    return render(requset, "user/register.html", {"form": form, "message": message})
