from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.users, name='home'),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
]