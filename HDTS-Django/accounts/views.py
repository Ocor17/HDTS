from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()
    return render(response, 'accounts/register.html', {"form":form})

@unauthenticated_user
def select_login_page(response):
    return render(response, 'accounts/select_login.html', {}) 

@unauthenticated_user
def requestor_login_page(response):
    form = AuthenticationForm()
    if response.method == "POST":
        username = response.POST['username']
        password = response.POST['password']
        
        user = authenticate(response, username=username, password=password)
        
        if user is not None:
            login(response, user)
            return redirect("/request")
        else:
            messages.info(response, "Username or password is incorrect")

    return render(response, 'accounts/requestorlogin.html', {"form":form})   

@unauthenticated_user
def maintainer_login_page(response):
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

    return render(response, 'accounts/maintainerlogin.html', {"form":form})   

def logout_user(response):
    logout(response)
    return redirect("/")