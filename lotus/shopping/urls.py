from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping, name='shopping'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_product_id>',
         views.remove_from_cart, name='remove_from_cart'),
]
