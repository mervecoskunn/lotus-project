from django.contrib import admin
from .models import Order, Rating

# Register your models here.
admin.site.register(Order)
admin.site.register(Rating)