# from django.models import models
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

class CreateNewRequest(forms.Form):
    classification_choices = (
        ("Classified", "Classified"),
        ("Unclassified", "Unclassified"),
    )

    connection_port = (
        ("SATA", "SATA"),
        ("M.2", "M.2"),
    )

    hd_type= (
        ("SSD", "SSD"),
        ("HDD", "HDD"),
    )

    event_type= (
        ("PMR", "PMR"),
        ("CVPA", "CVPA"),
        ("CVI", "CVI"),
        ("VoF", "VoF"),
        ("Research Project", "Research Project"),
    )

    event_status= (
        ("Confirmed", "Confirmed"),
        ("Forecasted", "Forecasted"),
        ("Canceled}", "Canceled"),
    )

    classification = forms.CharField(label="Classification", widget=forms.Select(choices=classification_choices))
    amount = forms.IntegerField(label="Amount required")
    port = forms.CharField(label="Connection Port Type",widget=forms.Select(choices=connection_port))
    size = forms.IntegerField(label="Hard Drive Size (MB)")
    type = forms.CharField(label="Hard Drive Type",widget=forms.Select(choices=hd_type))
    comment = forms.CharField(label="Comment")

    eventName = forms.CharField(label="Event Name", max_length=200)
    eventDescription = forms.CharField(label="Event Description")
    eventLocation = forms.CharField(label="Event Location", max_length=200)
    eventType = forms.CharField(label="Event Type",widget=forms.Select(choices=event_type))
    reportingCycle = forms.IntegerField(label="Length of Reporting Cycle (days)")
    eventStatus = forms.CharField(label="Event Status",widget=forms.Select(choices=event_status))
    eventStartDate = forms.DateField(label="Event Start Date")
    eventEndDate = forms.DateField(label="Event End Date")