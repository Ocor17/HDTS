from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(response, *args, **kwargs):
        if response.user.is_authenticated:
            return redirect("/Inventory")
        else:
            return view_func(response, *args, **kwargs)
    return wrapper_func