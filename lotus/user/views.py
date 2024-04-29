from django.shortcuts import render, redirect
from django.http import HttpResponse
from shopping.models import Product, product_list
from . import models as user_models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


@login_required
def favorites(request):
    context = {
        'favorites': []
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
    user_models.user1.remove_from_favorites(id)
    # TODO success message
    return redirect('favorites')


@login_required
def add_to_favorites(request, id):
    product = filter(lambda product: product.id == id, product_list)

    # TODO success message
    return render(request, 'user/favorites.html')
