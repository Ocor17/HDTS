from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(response, *args, **kwargs):
        return view_func(response, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            l = request.user.groups.values_list('name',flat = True)
            user_groups = list(l)

            if any(group in allowed_roles for group in user_groups):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Not Authorized')
        return wrapper_func
    return decorator