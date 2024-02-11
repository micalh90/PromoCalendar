from django.urls import path
from . import views

urlpatterns = [
path('', views.user_login),
path('create/', views.user_create),
]