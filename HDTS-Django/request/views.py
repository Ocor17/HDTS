from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateNewRequest
from .models import RequestList, Request
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def new_request(response):
    if response.method == "POST":
        form = CreateNewRequest(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = RequestList(name=n)
            t.save()
            response.user.requestlist.add(n)

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewRequest()

    return render(response, 'request/newrequest.html', {"form":form})

@login_required(login_url='/')
def request_list(response):
    return render(response, "request/requestlist.html")

@login_required(login_url='/')
def mainMenu(request):
    return render(request, 'request/mainmenu.html')