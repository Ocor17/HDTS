from datetime import datetime
from django.urls import reverse
from django.utils import timezone
import pytz
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
import pytz
from .forms import CreateNewRequest
from .models import RequestList
from .utils import calc_ret_date, gen_ticket_number, calc_req_num
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(response, id):
    ls = RequestList.objects.get(id=id)
    if ls in response.user.todolist.all():
        return render(response, 'request/requestlist.html', {"ls":ls})
    return render(response, 'accounts/requestorlogin.html', {})

@login_required(login_url='/')
def new_request(response):#will get values from user to generate new request in database
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
            hd_pick_up_date = form.cleaned_data['hd_pick_up_date']

            t = RequestList.objects.create(user=response.user, #takes the current id of the logged in user and sets it as a key for the request
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
                            requestStatus="pending",
                            ticket_number=gen_ticket_number(),
                            request_number=calc_req_num(),
                            request_creation_date=timezone.now(),
                            hd_pick_up_date=hd_pick_up_date,
                            hd_return_date=calc_ret_date(eventEndDate, reportingCycle)
                            )
            return redirect(reverse('request:requestlist'))
    else:
        form = CreateNewRequest()
    return render(response, 'request/newrequest.html', {"form":form})

@login_required(login_url='/')
def request_list(response):#passes values of requests made by current user
    ls = RequestList.objects.filter(user=response.user)
    return render(response, "request/requestlist.html", {"reqlist":ls})

@login_required(login_url='/')
def mainMenu(request):#passes user the default page
    return render(request, 'request/mainmenu.html')

@login_required(login_url='/')
def edit_request(request):
    return render(request, 'Edit Request')

@login_required(login_url='/')
def make_amendment(request):
    return render(request, 'Amend Request')