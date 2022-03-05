from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateNewRequest
from .models import RequestList, Request

# Create your views here.
def request(response):
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

    return render(response, 'request/request.html', {"form":form})

def requestList(response):
    return render(response, "request/requestlist.html")