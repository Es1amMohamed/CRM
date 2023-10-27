from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *

# Create your views here.


def home(request):
    records = Record.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect("/")
        else:
            messages.info(request, "Username or Password is incorrect")
            return render(request, "main_app/home.html")
    return render(request, "main_app/home.html", {"records": records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect("/")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect("/")
    else:
        form = SignUpForm()
        return render(request, "home/register.html", {"form": form})

    return render(request, "home/register.html", {"form": form})


def add_record(request):
    pass
