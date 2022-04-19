from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user
# Create your views here.

'''
Accounts Controller
    Handle the following routes
        - register [GET, POST]
        - select_login_page [GET]
        - requestor_login_page [GET, POST]
        - maintainer_login_page [GET, POST]
        - logout_user [GET]
'''

def accountRequest(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            #
            # group, created = Group.objects.get_or_create(name='maintainer')
            # user.groups.add(group)
            # group, created = Group.objects.get_or_create(name='test2')
            # user.groups.add(group)
            #
            return redirect("/")
    else:
        form = RegisterForm()
    return render(response, 'accounts/accountRequest.html', {"form":form})

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

@unauthenticated_user
def admin_login_page(response):
    form = AuthenticationForm()
    if response.method == "POST":
        username = response.POST['username']
        password = response.POST['password']
        
        user = authenticate(response, username=username, password=password)
        
        if user is not None:
            login(response, user)
            return redirect("/register")
        else:
            messages.info(response, "Username or password is incorrect")

    return render(response, 'accounts/adminlogin.html', {"form":form})   

def logout_user(response):
    logout(response)
    return redirect("/")