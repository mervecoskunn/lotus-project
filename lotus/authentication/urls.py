from django.contrib import admin
from django.urls import path
from . import views as authentication_views

urlpatterns = [
    path('login', authentication_views.login, name="login"),
    path('register', authentication_views.register, name="register"),
    path('logout', authentication_views.logout, name="logout"),
]
