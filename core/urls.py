# core/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('shortenURL.urls')),
    path('admin/', admin.site.urls),
]
