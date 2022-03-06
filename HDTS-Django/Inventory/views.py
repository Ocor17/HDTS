from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import HardDrive
from .forms import addNewHardDrive
@csrf_exempt
def addHardDrive(request):
    if request.method == 'POST':
        form = addNewHardDrive(request.POST, request.FILES)
        #print(form.cleaned_data)
        if form.is_valid():
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
                                          modDate=modDate)            #hd.save()
            return HttpResponse('Form Works!')
    return HttpResponse('Hello World!')

def viewInventory(request):
    #customer and product objects are passed. Values can be called from html
    harddrive = HardDrive.objects.all()
    return render(request, 'Inventory/viewInventory.html',{'harddrive':harddrive})

def mainMenu(request):
    return render(request, 'Inventory/mainMenu.html')