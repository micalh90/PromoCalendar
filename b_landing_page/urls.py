from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
path('', views.landing_page, name='home_page'),
path('login/', views.user_login, name='login_page'),
path('create/', views.user_create, name='create_user_page'),
path('', include('allauth.urls')),

]