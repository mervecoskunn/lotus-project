from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from shopping.models import Product
from . import models as user_models
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.


@login_required
def favorites(request):
    profile = User.objects.filter(
        username=request.user.username
    ).first().profile
    favorites = profile.favorites.all()
    context = {
        'favorites': favorites,
        'is_empty': len(favorites) == 0
    }
    return render(request, 'user/favorites.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        address = str(address).replace("\n", "").replace("\t", "").strip()
        user = User.objects.filter(
            username=request.user.username
        ).first()
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        user_profile = user.profile
        user_profile.address = address
        user_profile.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('profile')
    user_profile = User.objects.filter(
        username=request.user.username
    ).first().profile
    return render(request, 'user/profile.html', {'user_profile': user_profile})


@login_required
def settings(request):
    return HttpResponse("Settings page")
    # return render(request, 'user/settings.html')


@login_required
def remove_from_favorites(request, id):
    profile = User.objects.filter(
        username=request.user.username
    ).first().profile
    profile.remove_from_favorites(id)
    messages.success(request, 'Product removed from favorites')

    # Go back to the page where the user clicked the button
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def add_to_favorites(request, id):
    product = Product.objects.get(id=id)
    profile = User.objects.filter(
        username=request.user.username
    ).first().profile
    profile.add_to_favorites(product)
    messages.success(request, 'Product added to favorites')

    # Go back to the page where the user clicked the button
    return redirect(request.META.get('HTTP_REFERER', '/'))
