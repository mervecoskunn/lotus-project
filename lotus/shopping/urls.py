from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping, name='shopping')
]
