from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from . import models
from user.models import Profile
from .models import CartProduct
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import ProductForm
from .utils import (get_search_results, get_filter_results,
                    get_filter_key_values, sort_products, get_empty_filters, get_filter_values)


def shopping(request):
    if request.method == 'POST':
        if request.POST.get('remove_filters') is not None:
            product_list = models.Product.objects.all()
            p = Paginator(product_list, 6)
            page = request.GET.get('page')
            products = p.get_page(page)
            context = {
                "products": products,
                "filters": get_empty_filters()
            }
            return render(request, 'shopping/shopping.html', context)

        search_key = request.POST.get('search_key')
        filter_key_values = get_filter_key_values(request.POST)
        sort_option = request.POST.get('sort_option')
        print('sort_option', sort_option)
        if search_key is not None:
            search_results = get_search_results(search_key)
            p = Paginator(search_results, 6)
            page = request.GET.get('page')
            products = p.get_page(page)
            context = {
                "products": products,
                "filters": get_empty_filters(),
            }

        elif filter_key_values.__len__() > 0:
            filter_results = get_filter_results(filter_key_values)
            context = {
                "products": filter_results,
                "filters": get_filter_values(filter_results)
            }

        elif sort_option is not None:
            products = sort_products(sort_option)
            p = Paginator(products, 6)
            page = request.GET.get('page')
            products = p.get_page(page)
            context = {
                "products": products,
                "filters": get_empty_filters(),
                "sort_option": sort_option
            }

        else:
            context = {
                "products": [],
                "filters": get_empty_filters()
            }
    else:
        product_list = models.Product.objects.all()
        p = Paginator(product_list, 6)
        page = request.GET.get('page')
        products = p.get_page(page)
        context = {
            "products": products,
            "filters": get_empty_filters(),
        }
    return render(request, 'shopping/shopping.html', context)


def product_detail(request, product_id):
    product = models.Product.objects.get(id=product_id)
    if not request.user.is_anonymous:
        is_favorited = Profile.objects.get(
            user=request.user).favorites.filter(id=product_id).exists()
        is_added_to_cart = Profile.objects.get(
            user=request.user).cart.items.filter(product_id=product_id).exists()
        quantity = 1
        if is_added_to_cart:
            quantity = Profile.objects.get(user=request.user).cart.items.get(
                product_id=product_id).quantity
        context = {
            "product": product,
            "is_favorited": is_favorited,
            "is_added_to_cart": is_added_to_cart,
            "quantity": quantity
        }
    else:
        context = {
            "product": product,
            "quantity": 1
        }
    return render(request, 'shopping/product_detail.html', context)


@login_required
def cart(request):
    cart = Profile.objects.get(user=request.user).cart
    items = cart.items.all()
    context = {
        "cart": cart,
        "items": items,
        "is_empty": items.count() == 0
    }
    return render(request, 'shopping/cart.html', context)


@login_required
def add_to_cart(request):
    product_id = int(request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity'))
    post_type = request.POST.get('post_type')
    if post_type == 'update':
        product = models.Product.objects.get(id=product_id)
        cart = Profile.objects.get(user=request.user).cart
        cart_product = models.CartProduct.objects.get(
            product=product, cart=cart)
        cart_product.quantity = quantity
        cart_product.subtotal = product.price * quantity
        cart_product.save()
        cart_product.cart.recalculate()
        messages.success(request, 'Product quantity updated')

        return redirect(request.META.get('HTTP_REFERER', '/'))

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


@login_required
def add_product(request):
    print(request.POST)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully')
            return redirect('shopping')

    else:
        form = ProductForm()
    return render(request, 'shopping/add_product.html', {'form': form})


@login_required
def edit_product(request, product_id):
    product = models.Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect(reverse('product_detail', args=[product_id]))

    else:
        form = ProductForm(instance=product)
    return render(request, 'shopping/edit_product.html', {'form': form})


@login_required
def delete_product(request, product_id):
    product = models.Product.objects.get(id=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully')

    return redirect('shopping')


@login_required
def product_confirm_delete(request, product_id):
    product = models.Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'shopping/product_confirm_delete.html', context)
