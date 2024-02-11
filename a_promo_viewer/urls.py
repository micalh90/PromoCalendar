from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('b_landing_page.urls')),
    path('', include('allauth.urls')),
]
