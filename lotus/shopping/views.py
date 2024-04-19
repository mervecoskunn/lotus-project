from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.


def shopping(request):
    if request.method == 'POST':
        search_key = request.POST.get('search_key')
        search_results = filter(lambda product: search_key.lower() in product.name.lower(),
                                models.product_list)
        context = {
            "products": search_results
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
