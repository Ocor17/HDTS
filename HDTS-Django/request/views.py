from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateNewRequest
from .models import RequestList, Request
from django.contrib.auth.decorators import login_required

this_year = datetime.year
request_num = 1

# Create your views here.
def index(response, id):
    ls = RequestList.objects.get(id=id)

    if ls in response.user.todolist.all():
        return render(response, 'request/requestlist.html', {"ls":ls})
    return render(response, 'accounts/requestorlogin.html', {})

@login_required(login_url='/')
def new_request(response):
    if response.method == "POST":
        form = CreateNewRequest(response.POST)

        if form.is_valid():
            name = form.cleaned_data["eventName"]

            classification = form.cleaned_data["classification"]
            amount = form.cleaned_data["amount"]
            port = form.cleaned_data["port"]
            size = form.cleaned_data["size"]
            type = form.cleaned_data["type"]
            comment = form.cleaned_data["comment"]
            eventDescription = form.cleaned_data["eventDescription"]
            eventLocation = form.cleaned_data["eventLocation"]
            eventType = form.cleaned_data["eventType"]
            reportingCycle = form.cleaned_data["reportingCycle"]
            eventStatus = form.cleaned_data["eventStatus"]
            eventStartDate = form.cleaned_data["eventStartDate"]
            eventEndDate = form.cleaned_data["eventEndDate"]


            t = RequestList.objects.create(user=response.user, #takes the current id of the logged in user and sets it as a key for the request
                            req_id=str(this_year) + "/" +  str(request_num),  #sets Id of the request to YYYY/number of the request
                            name=name, 
                            classification=classification, 
                            amount=amount, 
                            port=port, 
                            size=size, 
                            type=type, 
                            comment=comment, 
                            eventDescription=eventDescription, 
                            eventLocation=eventLocation, 
                            eventType=eventType, 
                            reportingCycle=reportingCycle, 
                            eventStatus=eventStatus, 
                            eventStartDate=eventStartDate, 
                            eventEndDate=eventEndDate,
                            requestStatus="pending")

            if this_year != datetime.year:  #If a new year has started, start request from 0 again
                request_num = 0
                this_year = datetime.year
            else:
                request_num += 1

            #t.save()
            #response.user.requestlist.add(t)
    else:
        form = CreateNewRequest()
    return render(response, 'request/newrequest.html', {"form":form})

@login_required(login_url='/')
def request_list(response):
    ls = RequestList.objects.filter(user=response.user)#only get list of request made by current user
    return render(response, "request/requestlist.html", {"reqlist":ls})

@login_required(login_url='/')
def mainMenu(request):
    return render(request, 'request/mainmenu.html')