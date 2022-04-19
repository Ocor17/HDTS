from urllib import response
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.template import loader

from .forms import addNewHardDrive
from .models import HardDrive
from .forms import addNewHardDrive
from request.models import RequestList

from datetime import date

import logging,traceback
logger = logging.getLogger('django')

'''
Hard Drive Inventory Controller
    Handle the following routes
        - AddHardDrive [GET, POST]
        - viewInventory [GET]
        - mainMenu [GET]
        - goto_request [GET]

'''

@csrf_exempt
@login_required(login_url='/') 
def addHardDrive(request):
    context ={}
    if request.method == 'POST':
        form = addNewHardDrive(request.POST or None, request.FILES or None)
        #print(form.cleaned_data)
        if form.is_valid():
           form.save()      
    else:
        form = addNewHardDrive()
    
    context['form'] = form
    logger.info('Hard Drive Added')
    return render(request, 'Inventory/addHardDrive.html', context) 


@login_required(login_url='/')
def viewInventory(request):
    #customer and product objects are passed. Values can be called from html

    '''
    filters = {
        key: value
        for key, value in request.post.items()
        if key in ['creationDate', 'serialNo', 'manufacturer','modelNo', 'hdType', 
        'connPort', 'hdSize', 'hdClass', 'justiClass', 'imageVerID', 'btStatus',
        'btExpDate', 'hdStatus', 'justiStatus', 'issueDate', 'expectRetDate', 
        'justiRetDate', 'actualRetDate', 'modDate',]
        #['user', 'modifier', 'reqRefNo', 'expression']
    }
    '''

    harddrive = HardDrive.objects.all()
    #call inventory html and pass 'harddrive' as an object to be itterated through
    return render(request, 'Inventory/viewInventory.html',{'harddrive':harddrive})

def write_file_contents():
    f = open('./logs/log.log', 'r')
    file_contents = f.read().splitlines()
    #print(file_contents)
    f.close()
    return file_contents

@login_required(login_url='/')
def viewLog(request):
    file_contents = write_file_contents()
    harddrive = HardDrive.objects.all()
    return render(request, 'Inventory/viewLog.html',{'harddrive':harddrive, 'file_contents':file_contents})

@login_required(login_url='/')
def mainMenu(request):
    return render(request, 'Inventory/mainMenu.html')


@login_required(login_url='/')
def view_request(response):#passes request values stored to be called from html
    ls = RequestList.objects.all()
    return render(response, "Inventory/viewrequest.html", {"reqlist":ls})


@login_required(login_url='/')
def viewHardDrive(request, sn):
    hd = HardDrive.objects.get(serialNo=sn)
    return render(request, "Inventory/viewHardDrive.html", {'hd': hd})


@login_required(login_url='/')
def updateHardDrive(request, sn):
    hd = HardDrive.objects.filter(serialNo=sn).first()

    if request.method == 'POST':
        form = addNewHardDrive(request.POST, instance=hd)
        if form.is_valid():
            form.save()
    else:
        form = addNewHardDrive(instance=hd)

    return render(request, "Inventory/updatedHardDrive.html", {'form': form, 'sn': sn})
