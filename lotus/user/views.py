from django.shortcuts import render, redirect
from django.http import HttpResponse
from shopping.models import Product, product_list
from . import models as user_models

# Create your views here.


def favorites(request):
    context = {
        'favorites': user_models.user1.favorites
    }
    return render(request, 'user/favorites.html', context)


def profile(request):
    return HttpResponse("Profile page")
    # return render(request, 'user/profile.html')


def settings(request):
    return HttpResponse("Settings page")
    # return render(request, 'user/settings.html')


def remove_from_favorites(request, id):
    user_models.user1.remove_from_favorites(id)
    # TODO success message
    return redirect('favorites')


def add_to_favorites(request, id):
    product = filter(lambda product: product.id == id, product_list)
    user_models.user1.add_to_favorites(product)

    # TODO success message
    return render(request, 'user/favorites.html')
