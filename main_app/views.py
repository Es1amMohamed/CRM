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
    form = AddRecordForm(request.POST or None)
    if request.method == "POST":
        if request.user.is_authenticated:
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added...")
                return redirect("/")
        else:
            messages.success(request, "You Must Be Logged In...")
            return redirect("/")
    return render(request, "main_app/add_record.html", {"form": form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(
            request, "main_app/record.html", {"customer_record": customer_record}
        )
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect("/")


def update_record(request, pk):
    current_record = Record.objects.get(id=pk)
    form = AddRecordForm(request.POST or None, instance=current_record)
    if request.user.is_authenticated:
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect("/")
    else:
        messages.success(request, "You Must Be Logged In To Do That ")
        return redirect("/")
    return render(request, "main_app/update_record.html", {"form": form})


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted Successfully ")
        return redirect("/")
    else:
        messages.success(request, "You Must Be Logged In To Do That ")
        return redirect("/")
