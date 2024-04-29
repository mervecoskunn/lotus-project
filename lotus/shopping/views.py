from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.

filter_keys = [
    'bracelet', 'pendulum', 'natural-stones', 'incense', 'chackra-stones'
]

sort_options = [
    'date-added-low-to-high', 'date-added-high-to-low',
    'price-low-to-high', 'price-high-to-low',
    'name-a-z', 'name-z-a'
]


@login_required
def get_filter_key_values(post_data) -> list:
    return list(filter(lambda key: post_data.get(key) is not None,
                       [post_data.get(key) for key in filter_keys]))


@login_required
def get_search_results(search_key) -> list:
    return filter(lambda product: search_key.lower() in product.name.lower(),
                  models.product_list)


@login_required
def get_filter_results(filter_key_values) -> list:
    filter_results = []
    for filter_key in filter_key_values:
        filter_results += list(filter(lambda product: product.category.lower() == filter_key.lower(),
                                      models.product_list))
    return filter_results


@login_required
def sort_products(order_by) -> list:
    if order_by == 'price-low-to-high':
        return sorted(models.product_list, key=lambda product: product.price)
    elif order_by == 'price-high-to-low':
        return sorted(models.product_list, key=lambda product: product.price, reverse=True)
    elif order_by == 'name-a-z':
        return sorted(models.product_list, key=lambda product: product.name)
    elif order_by == 'name-z-a':
        return sorted(models.product_list, key=lambda product: product.name, reverse=True)
    else:
        return []


@login_required
def shopping(request):
    # TODO Remove this line
    #              models.add_products()
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
    product = models.product_list[product_id]
    context = {
        "product": product
    }
    return render(request, 'shopping/product_detail.html', context)


@login_required
def cart(request):
    context = {
        "cart": models.carts[0]
    }
    return render(request, 'shopping/cart.html', context)


@login_required
def add_to_cart(request):
    product_id = int(request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity'))
    product = models.product_list[product_id]
    cart_product = models.CartProduct(product, quantity)
    models.carts[0].add_product(cart_product)

    # TODO Success message
    return HttpResponse("Added to cart")


@login_required
def remove_from_cart(request, product_id):

    models.carts[0].remove_product(product_id)
    context = {
        "cart": models.carts[0]
    }
    # TODO Success message
    return redirect('cart')
