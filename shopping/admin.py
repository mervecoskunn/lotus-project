from django.contrib import admin
from .models import Product, CartProduct, Cart

# Register your models here.
admin.site.register(Product)
admin.site.register(CartProduct)
admin.site.register(Cart)
