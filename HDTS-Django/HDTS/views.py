from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import addNewHardDrive

from django.views.decorators.csrf import csrf_exempt
from .models import HardDrive

@csrf_exempt
def addHardDrive(request):
    if request.method == 'POST':
        form = addNewHardDrive(request.POST)
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

            hd = HardDrive(creationDate, serialNo, manufacturer, modelNo, hdType, connPort, hdSize, hdClass, justiClass, imageVerID, btStatus, btExpDate, hdStatus,
                justiStatus, issueDate, expectRetDate, justiRetDate, actualRetDate, modDate)
            hd.save()
            return HttpResponse('Form Works!')
    return HttpResponse('Hello World!')