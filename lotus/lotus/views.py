from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'lotus/home.html')


def contact(request):
    return render(request, 'lotus/contact.html')


def contact(request):
    return HttpResponse("Contact Page")
    # return render(request, 'lotus/contact.html')


# TODO will be moved to user app (user app will be created)
def profile(request):
    return HttpResponse("Profile Page")
    # return render(request, 'lotus/profile.html')


# TODO will be moved to user app (user app will be created)
def favorites(request):
    return HttpResponse("Favorites Page")
    # return render(request, 'lotus/favorites.html')
