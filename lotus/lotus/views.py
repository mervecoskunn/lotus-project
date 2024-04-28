from django.shortcuts import render
from django.http import HttpResponse
from blog import models
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {
        'latest_blogs': models.post_list[:3]
    }
    return render(request, 'lotus/home.html', context)


@login_required
def contact(request):
    return render(request, 'lotus/contact.html')
