from django.shortcuts import render
from django.http import HttpResponse
from blog import models


def home(request):
    context = {
        'latest_blogs': models.post_list[:3]
    }
    return render(request, 'lotus/home.html', context)


def contact(request):
    return render(request, 'lotus/contact.html')


def contact(request):
    return render(request, 'lotus/contact.html')
