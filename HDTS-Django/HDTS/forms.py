from email.policy import default
from random import choice
from django import forms
import datetime
from .choices import *
#from .models import HardDrive



class addNewHardDrive(forms.Form):
    """ 
    Revisit Later
    reportLifecycle = 17
    eventEndDate = datetime.date(2022, 2, 28)
    today = datetime.date.today()
    reportLifecyleDays = datetime.timedelta(days=reportLifecycle)
    endDateDays = (eventEndDate - datetime.date.today()).days
    endDateDays2 = datetime.timedelta(days=endDateDays) 
    calculated_date = today + reportLifecyleDays + endDateDays2 """

    creationDate = forms.DateField(label='Creation Date', label_suffix='MM/DD/YYYY', initial=datetime.date.today)
    serialNo = forms.IntegerField(label='Serial Number')
    manufacturer = forms.ChoiceField(label='Manufacturer', choices=MANUFACTURER_CHOICES[0], required=False)
    modelNo = forms.IntegerField(label='Model Number', required=False)
    hdType = forms.ChoiceField(label=' Hard Drive Type', choices=HD_TYPE_CHOICES)
    connPort = forms.ChoiceField(label=' Hard Drive Connection Port', choices=CONN_PORT_CHOICES)
    hdSize = forms.ChoiceField(label='Hard Drive Size', choices=HD_MEMORY_SIZES)
    hdClass = forms.ChoiceField(label=' Hard Drive Classification', choices=CLASS_CHOICES, required=False)
    justiClass = forms.FileField(label='Justification for Classification Change', required=False)
    imageVerID = forms.IntegerField(label='Image Version ID', max_value=9999, min_value=0, required=False)
    btStatus = forms.BooleanField(label='Boot Test Passed?', required=False)
    btExpDate = forms.DateField(label='Boot Expiration Date', label_suffix='MM/DD/YYYY', initial=datetime.date.today, required=False)
    hdStatus = forms.ChoiceField(label='HD Status', choices=HD_STATUS_CHOICES)
    justiStatus = forms.FileField(label='Justification Change Status', required=False)
    issueDate = forms.DateField(label='Issue Date', label_suffix='MM/DD/YYYY', initial=datetime.date.today, required=False)
    expectRetDate = forms.DateField(label='Expected Returned Date', label_suffix='MM/DD/YYYY',  required=False)
    justiRetDate = forms.FileField(label='Justification Change Return Date', required=False)
    actualRetDate = forms.DateField(label='Actual Returned Date', label_suffix='MM/DD/YYYY', initial=datetime.date.today)
    modDate = forms.DateField(label='Modified Date', label_suffix='MM/DD/YYYY', initial=datetime.date.today)

    #class Meta:
    #   model = HardDrive
    #   fiels = ['creationDate', 'serialNo', 'manufacturer',
    #  'modelNo', 'hdType', 'connPort', 'hdSize', 'hdClass', 'justiClass', 'imageVerID', 
    # 'btStatus', 'btExpDate', 'hdStatus', 'justiStatus', 'issueDate', 'expectRetDate', 'justiRetDate', 'actualRetDate', 'modDate']