# from django.models import models
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

class CreateNewRequest(forms.Form):
    classification_choices = (
        (1, "Classified"),
        (2, "Unclassified"),
    )

    connection_port = (
        (1, "SATA"),
    )

    hd_type= (
        (1, "type1"),
        (2, "type2"),
    )

    event_type= (
        (1, "type1"),
        (2, "type2"),
    )

    event_status= (
        (1, "type1"),
        (2, "type2"),
    )

    classification = forms.CharField(label="Classification", widget=forms.Select(choices=classification_choices))
    amount = forms.IntegerField(label="Amount required")
    port = forms.CharField(label="Connection Port Type",widget=forms.Select(choices=connection_port))
    size = forms.IntegerField(label="Hard Drive Size (MB)")
    type = forms.CharField(label="Hard Drive Type",widget=forms.Select(choices=hd_type))
    comment = forms.CharField(label="Comment")

    eventName = forms.CharField(label="Event Name")
    eventDescription = forms.CharField(label="Event Description")
    eventLocation = forms.CharField(label="Event Location")
    eventType = forms.CharField(label="Event Type",widget=forms.Select(choices=event_type))
    reportingCycle = forms.IntegerField(label="Length of Reporting Cycle (days)")
    eventStatus = forms.CharField(label="Event Status",widget=forms.Select(choices=event_status))
    eventStartDate = forms.DateField(label="Event Start Date")
    eventEndDate = forms.DateField(label="Event End Date")