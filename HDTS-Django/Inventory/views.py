from urllib import response
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .forms import addNewHardDrive, return_hard_drives
from .models import HardDrive
from .forms import addNewHardDrive
from request.models import RequestList

from datetime import date

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
    return render(request, 'Inventory/addHardDrive.html', context) 


@login_required(login_url='/')
def viewInventory(request):
    #customer and product objects are passed. Values can be called from html
    harddrive = HardDrive.objects.all()
    #call inventory html and pass 'harddrive' as an object to be itterated through
    return render(request, 'Inventory/viewInventory.html',{'harddrive':harddrive})


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

    a = HardDrive.objects.get(serialNo=sn)
    if request.method == 'POST':
        print(0)
        form = addNewHardDrive(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return redirect('viewInventory/')
    else:
        print(1)
        form = addNewHardDrive(instance=a)

    return render(request, "Inventory/updatedHardDrive.html", {'form': form, 'sn': sn})

@login_required(login_url='/')
def return_hard_drive(response):
    hd_formSet = formset_factory(return_hard_drives)
    formset = hd_formSet(response.POST or None)
    if response.method == 'POST':
        if formset.is_valid():  
            for form in formset:
                form = form.cleaned_data
                serial_num = form.get('serialNo')
                hd = HardDrive.objects.get(serialNo=serial_num)
                hd.hdStatus = 'Pending Wipe'
                hd.save(update_fields=['hdStatus'])
        return redirect(reverse('Inventory:viewInventory'))

    
    return render(response, "Inventory/return.html", {'formset': formset})