from email.policy import default
from random import choice
from urllib import request
from django import forms
import datetime
from .choices import *
from .models import HardDrive
from django.utils.translation import gettext_lazy as _

'''
This class is the form used to add a Hard Drive
    This verifies whether the inputs that the user provided were correct
    If they were it proceeds to insert the Hard Drive onto the server
'''

class addNewHardDrive(forms.ModelForm):
    creationDate = forms.DateField(label='Creation Date', initial=datetime.date.today, disabled=True)
    imageVerID = forms.IntegerField(label='Image Version ID', max_value=9999, min_value=0, required=False)

    class Meta:
        model = HardDrive
        fields = ['creationDate', 'serialNo', 'manufacturer',
        'modelNo', 'hdType', 'connPort', 'hdSize', 'hdClass', 'justiClass', 'imageVerID', 
        'btStatus', 'btExpDate', 'hdStatus', 'justiStatus', 'issueDate', 'expectRetDate', 'justiRetDate', 'actualRetDate', 'modDate']
        labels = {
            'serialNo': _('Serial Number'),
            'manufacturer': _('Manufacturer'),
            'modelNo': _('Model Number'),
            'hdType': _('Hard Drive Type'),
            'connPort': _('Hard Drive Connection Port'),
            'hdSize': _('Hard Drive Size'),
            'hdClass': _('Hard Drive Classification'),
            'justiClass': _('Justification for Classification Change'),
            'btStatus': _('Boot Test Passed?'),
            'btExpDate': _('Boot Test Expiration Date'),
            'hdStatus': _('Hard Drive Status'),
            'justiStatus': _('Justification for Status Change'),
            'issueDate': _('Issue Date'),
            'expectRetDate': _('Expected Return Date'),
            'justiRetDate': _('Justification for Return Date Change'),
            'actualRetDate': _('Actual Return Date'),
            'modDate': _('Modified Date'),
        }

        widgets = {
            'btStatus': forms.RadioSelect(choices=BOOT_TEST_CHOICES),
            'btExpDate': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),
            'issueDate': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),
            'expectRetDate': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),
            'actualRetDate': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),
            'modDate': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),
        }