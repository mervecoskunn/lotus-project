from django.contrib import admin
from django.urls import path
from . import views as users_views

urlpatterns = [
    path('/login', users_views.login, name="login"),
    path('/register', users_views.register, name="register"),
]
