from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from shopping.models import Product
from . import models as user_models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


@login_required
def favorites(request):
    profile = User.objects.filter(
        username=request.user.username
    ).first().profile
    context = {
        'favorites': profile.favorites.all()
    }
    return render(request, 'user/favorites.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        user_models.user1.profile.address = address
        user_models.user1.profile.save()
        # TODO Success message
        return redirect('profile')
    profile = User.objects.filter(
        username=request.user.username
    ).first().profile
    return render(request, 'user/profile.html', {'profile': profile})


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
