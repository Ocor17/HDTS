from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import addNewHardDrive
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt

from .models import HardDrive
from .forms import addNewHardDrive
from request.models import RequestList

@csrf_exempt
@login_required(login_url='/') 
def addHardDrive(request):
    if request.method == 'POST':
        form = addNewHardDrive(request.POST, request.FILES)
        #print(form.cleaned_data)
        if form.is_valid():
            if not HardDrive.objects.filter(serialNo = form.cleaned_data['serialNo']).exists():
                creationDate = form.cleaned_data['creationDate']
                serialNo = form.cleaned_data['serialNo']
                manufacturer = form.cleaned_data['manufacturer']
                modelNo = form.cleaned_data['modelNo']
                hdType = form.cleaned_data['hdType']
                connPort = form.cleaned_data['connPort']
                hdSize = form.cleaned_data['hdSize']
                hdClass = form.cleaned_data['hdClass']
                justiClass = form.cleaned_data['justiClass']
                imageVerID = form.cleaned_data['imageVerID']
                btStatus = form.cleaned_data['btStatus']
                btExpDate = form.cleaned_data['btExpDate']
                hdStatus = form.cleaned_data['hdStatus']
                justiStatus = form.cleaned_data['justiStatus']
                issueDate = form.cleaned_data['issueDate']
                expectRetDate = form.cleaned_data['expectRetDate']
                justiRetDate = form.cleaned_data['justiRetDate']
                actualRetDate = form.cleaned_data['actualRetDate']
                modDate = form.cleaned_data['modDate'] 

                hd = HardDrive.objects.create(creationDate=creationDate, 
                                            serialNo=serialNo, 
                                            manufacturer=manufacturer, 
                                            modelNo=modelNo,
                                            hdType=hdType, 
                                            connPort=connPort, 
                                            hdSize=hdSize, 
                                            hdClass=hdClass, 
                                            justiClass=justiClass, 
                                            imageVerID=imageVerID, 
                                            btStatus=btStatus,
                                            btExpDate=btExpDate, 
                                            hdStatus=hdStatus, 
                                            justiStatus=justiStatus, 
                                            issueDate=issueDate, 
                                            expectRetDate=expectRetDate,
                                            justiRetDate=justiRetDate, 
                                            actualRetDate=actualRetDate, 
                                            modDate=modDate)           
                return HttpResponse('Hard Drive added to Inventory!')
            else:
                return HttpResponse('Hard Drive alreadys exists')
    return HttpResponse('Failed to add Hard Drive!')

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
def view_request(response):
    ls = RequestList.objects.all()
    return render(response, "Inventory/viewrequest.html", {"reqlist":ls})