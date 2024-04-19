from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

filter_keys = [
    'bracelet', 'pendulum', 'natural-stones', 'incense', 'chackra-stones'
]


def get_filter_key_values(post_data) -> list:
    return list(filter(lambda key: post_data.get(key) is not None,
                       [post_data.get(key) for key in filter_keys]))


def get_search_results(search_key) -> list:
    return filter(lambda product: search_key.lower() in product.name.lower(),
                  models.product_list)


def get_filter_results(filter_key_values) -> list:
    filter_results = []
    for filter_key in filter_key_values:
        filter_results += list(filter(lambda product: product.category.lower() == filter_key.lower(),
                                      models.product_list))
    return filter_results


def shopping(request):
    if request.method == 'POST':
        search_key = request.POST.get('search_key')
        filter_key_values = get_filter_key_values(request.POST)
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

    else:
        context = {
            "products": models.product_list
        }
    return render(request, 'shopping/shopping.html', context)


def product_detail(request, product_id):
    product = models.product_list[product_id]
    context = {
        "product": product
    }
    return render(request, 'shopping/product_detail.html', context)


def cart(request):
    return HttpResponse("Cart Page")
    # return render(request, 'shopping/cart.html')
