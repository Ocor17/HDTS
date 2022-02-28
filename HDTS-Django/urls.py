from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('HDTS/', include('HDTS.urls')),
    path('admin/', admin.site.urls),
    path('', include('HDTS.urls')),
]