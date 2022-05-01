from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
# from .forms import addNewHardDrive
from accounts.models import User
# from .forms import addNewHardDrive
from request.models import RequestList
# from accounts

@login_required(login_url='/')
def viewAccounts(request):
    #customer and product objects are passed. Values can be called from html
    userAccounts = User.objects.all()
    #call inventory html and pass 'harddrive' as an object to be itterated through
    return render(request, 'register/viewAccounts.html',{'accounts':userAccounts})

# def requestAdmin(request):
#     return render(request, 'register/viewAccounts.html',{'accounts':userAccounts})

def requestAdmin(response):
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
            # return redirect("/")
    else:
        form = RegisterForm()
    return render(response, 'register/accountRequestAdmin.html', {"form":form})

@login_required(login_url='/')
def mainMenu(request):
    return render(request, 'register/mainMenu.html')