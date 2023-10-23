from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect( "/")
        else:
            messages.info(request, "Username or Password is incorrect")
            return render(request, "main_app/home.html")
    return render(request, "main_app/home.html")


def login_user(request):
    pass

def logout_user(request):
    pass