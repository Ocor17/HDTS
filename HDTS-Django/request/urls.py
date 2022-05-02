"""HDTS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
app_name = 'request'
urlpatterns = [
    path('', views.request_list, name='requestlist'),
    path('newrequest/', views.new_request, name='newrequest'),
    path('requestlist/', views.request_list, name='requestlist'),
    path('requestlist/<request_id>', views.request_list, name='requestlistparams'),
    path('<str>:<int>', views.index, name='index'),
    path('editrequest/<request_number>', views.edit_request, name='editrequest'),
    path('clonerequest/<request_number>', views.clone_request, name='clonerequest'),
]