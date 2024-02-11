from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
path('admin/', admin.site.urls),
path('', views.landing_page),
path('login/', include('b_user_auth.urls')),

]