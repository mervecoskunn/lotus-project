from django.shortcuts import render
from django.http import HttpResponse
from blog import models
from django.contrib.auth.decorators import login_required


def home(request):
    latest_posts = models.Post.objects.all().order_by('-date_posted')
    if len(latest_posts) > 3:
        latest_posts = latest_posts[:3]
    context = {
        'latest_posts': latest_posts
    }
    return render(request, 'lotus/home.html', context)


def contact(request):
    return render(request, 'lotus/contact.html')


def privacy_policy(request):
    return render(request, 'lotus/privacy-policy.html')


def faq(request):
    return render(request, 'lotus/faq.html')


def custom_500(request):
    return render(request, '500.html')
