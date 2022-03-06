from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = RegisterForm()
    return render(response, 'accounts/register.html', {"form":form})

def login_page(response):
    if response.user.is_authenticated:
        return redirect("/Inventory")
    else:
        form = AuthenticationForm()
        if response.method == "POST":
            username = response.POST['username']
            password = response.POST['password']
            
            user = authenticate(response, username=username, password=password)
            
            if user is not None:
                login(response, user)
                return redirect("/Inventory")
            else:
                messages.info(response, "Username or password is incorrect")

        return render(response, 'accounts/login.html', {"form":form})    

def logout_user(response):
    logout(response)
    return redirect("/")