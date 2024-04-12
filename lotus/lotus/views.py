from django.shortcuts import render


def home(request):
    return render(request, 'lotus/home.html')


def contact(request):
    return render(request, 'lotus/contact.html')
