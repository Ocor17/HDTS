from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from datetime import date

'''
Form used to validated the inputes from the user,
    The password requirements are stored in the following file: 'HDTS-Django/HDTS/settings.py', under 'AUTH_PASSWORD_VALIDATORS
'''

class RegisterForm(UserCreationForm):
    role_choices = [
    ('Requestor', 'Requestor'),
    ('Maintainer', 'Maintainer'),
    ('Administrator', 'Administrator'),
    ('Auditor', 'Auditor'),
    ]

    user_status = [
    ('Pending', 'Pending'),
    ('Active', 'Active'),
    ('Disabled', 'Disabled'),
    ('Archived', 'Archived'),
    ]

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    user_role = forms.CharField(widget=forms.Select(choices=role_choices))
    direct_supervisor_email = forms.CharField(required=True)
    branch_chief_name = forms.CharField(required=True)
    approved = False
    last_modified_date = date.today()
    user_profile_status = forms.CharField(widget=forms.Select(choices=user_status))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2", "user_role", "direct_supervisor_email", "branch_chief_name"]
        
