from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/Inventory")
    else:
        form = RegisterForm()
    return render(response, 'accounts/register.html', {"form":form})

def login(response):
    if response.method == "POST":
        form = AuthenticationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/Inventory")
    else:
        form = AuthenticationForm()
    return render(response, 'accounts/login.html', {"form":form})    
