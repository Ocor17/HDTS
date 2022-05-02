from datetime import datetime
import re
from django.urls import reverse
from django.utils import timezone
import pytz
from urllib import response
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict

from .utils import calc_ret_date, gen_ticket_number, calc_req_num
from .forms import CreateNewRequest
from .models import RequestList
from .filters import RequestFilter

view_request = False
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
            eventName = form.cleaned_data["eventName"]
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
                            eventName=eventName, 
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
def request_list(response, request_id=None):#passes values of requests made by current user
    request_list = RequestList.objects.filter(user=response.user).order_by('eventName')
    request = None

    if request_id is not None:
        filter = {}
        filter['request_number'] = request_id
        request = RequestList.objects.filter(**filter)  

    filter = RequestFilter(response.GET, queryset=request_list)
    request_list = filter.qs
    
    paginator = Paginator(request_list, 5)

    page_number = response.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #print(request)
    return render(response, "request/requestlist.html", 
        {"reqlist":request_list, 'page_obj': page_obj, 
        'filter': filter, 'view_request': view_request, 'request':request})

@login_required(login_url='/')
def mainMenu(request):#passes user the default page
    return render(request, 'request/mainmenu.html')

def get_request(response, request_name):
    global view_request
    view_request = True
    filter = {}
    filter['name'] = request_name
    print(f'view_request: {view_request}')
    request = RequestList.objects.filter(**filter)

    return HttpResponse('done')
    #return render(response, "/", 
    #     {'req': request[0], 'user' :response.user, 'view_request': view_request})

@login_required(login_url='/')
def clone_request(response, request_number):
    request = RequestList.objects.filter(request_number=request_number).first()
    if response.method == 'POST':
        request.ticket_number=gen_ticket_number()
        request.request_number=calc_req_num()
        cloned_data=model_to_dict(request)
        form = CreateNewRequest(response.POST, initial=cloned_data)
        if form.is_valid():
            form.save()
    else:
        form = CreateNewRequest(instance=request)

    return render(response, "Request/newrequest.html", {'form': form, 'request_number': request_number})


@login_required(login_url='/')
def edit_request(response, request_number):
    request = RequestList.objects.filter(request_number=request_number).first()
    if request.requestStatus == 'pending':
        #request_qs = serializers.serialize('json', request)

        if response.method == 'POST':
            form = CreateNewRequest(response.POST, instance=request)
            if form.is_valid():
                form.save()
                redirect(reverse('request:requestlist'))
        else:
            form = CreateNewRequest(instance=request)
        return render(response, "Request/newrequest.html", {'form': form, 'request_number': request_number})
    return HttpResponse('Request is not pending')