from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'lotus/home.html')


def contact(request):
    return render(request, 'lotus/contact.html')


def contact(request):
    return render(request, 'lotus/contact.html')
