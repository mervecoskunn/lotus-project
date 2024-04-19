from django.shortcuts import render
from . import models
# Create your views here.


def shopping(request):
    context = {
        "products": models.product_list
    }
    return render(request, 'shopping/shopping.html', context)
