from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def user_register(requset):
    form = UserCreationForm()
    if requset.method == "POST":
        form = UserCreationForm(requset.POST)
        username = requset.POST.get("username")
        password1 = requset.POST.get("password1")
        password2 = requset.POST.get("password2")
        print(username, password1, password2)

    return render(requset, "user/register.html", {"form": form})
