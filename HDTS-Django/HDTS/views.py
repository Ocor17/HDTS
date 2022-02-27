from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import addNewHardDrive

#from .models import HardDrive

def addHardDrive(request):
    if request.method == 'POST':
        form = addNewHardDrive(request.POST)
        print(form.cleaned_data)
        if form.is_valid():
            pass
            """creationDate = form.cleaned_data['']
            serialNo = form.cleaned_data['']
            manufacturer = form.cleaned_data['']
            modelNo = form.cleaned_data['']
            hdType = form.cleaned_data['']
            connPort = form.cleaned_data['']
            hdSize = form.cleaned_data['']
            hdClass = form.cleaned_data['']
            justiClass = form.cleaned_data['']
            imageVerID = form.cleaned_data['']
            btStatus = form.cleaned_data['']
            btExpDate = form.cleaned_data['']
            hdStatus = form.cleaned_data['']
            justiStatus = form.cleaned_data['']
            issueDate = form.cleaned_data['']
            expectRetDate = form.cleaned_data['']
            justiRetDate = form.cleaned_data['']
            actualRetDate = form.cleaned_data['']
            modDate = form.cleaned_data[''] """
        
    return HttpResponse('Hello World!')