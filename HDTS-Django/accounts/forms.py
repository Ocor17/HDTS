from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

'''
Form used to validated the inputes from the user,
    The password requirements are stored in the following file: 'HDTS-Django/HDTS/settings.py', under 'AUTH_PASSWORD_VALIDATORS
'''

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
