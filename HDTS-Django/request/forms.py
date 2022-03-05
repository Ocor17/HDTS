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

    classification = forms.TypedMultipleChoiceField(label="Classification",choices=classification_choices) 
    amount = forms.IntegerField(label="Amount required")
    port = forms.TypedMultipleChoiceField(label="Connection Port Type",choices=connection_port)
    size = forms.IntegerField(label="Hard Drive Size (MB)")
    type = forms.TypedMultipleChoiceField(label="Hard Drive Type",choices=hd_type)
    comment = forms.CharField(label="Comment")
