from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from . import models
from user.models import Profile
from .models import CartProduct
from django.contrib.auth.decorators import login_required
from .utils import get_search_results, get_filter_results, get_filter_key_values, sort_products


@login_required
def shopping(request):
    if request.method == 'POST':
        search_key = request.POST.get('search_key')
        filter_key_values = get_filter_key_values(request.POST)
        order_by = request.POST.get('sort_option')
        if search_key is not None:
            search_results = get_search_results(search_key)
            context = {
                "products": search_results
            }
        elif filter_key_values.__len__() > 0:
            filter_results = get_filter_results(filter_key_values)
            context = {
                "products": filter_results
            }
        elif order_by is not None:
            products = sort_products(order_by)
            context = {
                "products": products
            }

        else:
            context = {
                "products": []
            }
    else:
        context = {
            "products": models.Product.objects.all()
        }
    return render(request, 'shopping/shopping.html', context)


@login_required
def product_detail(request, product_id):
    product = models.Product.objects.get(id=product_id)
    is_favorited = Profile.objects.get(
        user=request.user).favorites.filter(id=product_id).exists()
    context = {
        "product": product,
        "is_favorited": is_favorited
    }
    return render(request, 'shopping/product_detail.html', context)


@login_required
def cart(request):
    cart = Profile.objects.get(user=request.user).cart
    context = {
        "cart": cart,
        "items": cart.items.all()
    }
    return render(request, 'shopping/cart.html', context)


@login_required
def add_to_cart(request):
    product_id = int(request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity'))
    product = models.Product.objects.get(id=product_id)
    cart_product = models.CartProduct.objects.create(
        product=product, quantity=quantity, subtotal=product.price * quantity)
    profile = Profile.objects.get(user=request.user)
    profile.cart.add_product(cart_product)
    profile.save()

    messages.success(request, 'Product added to cart')

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def remove_from_cart(request, cart_product_id):
    cart = Profile.objects.get(user=request.user).cart
    cart.remove_product(cart_product_id)
    messages.success(request, 'Product removed from cart')

    return redirect('cart')


@login_required
def increase_quantity(request, cart_product_id):
    cart = Profile.objects.get(user=request.user).cart
    if cart.increase_quantity(cart_product_id):
        messages.success(request, 'Product quantity increased by one')
    else:
        messages.error(request, 'Error increasing product quantity')

    return redirect('cart')


@login_required
def decrease_quantity(request, cart_product_id):
    cart_product = CartProduct.objects.get(id=cart_product_id)
    cart = Profile.objects.get(user=request.user).cart
    cart.decrease_quantity(cart_product_id)
    if cart_product.quantity == 1:
        messages.success(request, 'Product removed from cart')

        return redirect('cart')

    messages.success(request, 'Product quantity decreased by one')

    return redirect('cart')
