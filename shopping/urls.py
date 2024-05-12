from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping, name='shopping'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_product_id>',
         views.remove_from_cart, name='remove_from_cart'),
    path('increase-quantity/<int:cart_product_id>',
         views.increase_quantity, name='increase_quantity'),
    path('decrease-quantity/<int:cart_product_id>',
         views.decrease_quantity, name='decrease_quantity'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:product_id>/',
         views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/',
         views.delete_product, name='delete_product'),
    path('product_confirm_delete/<int:product_id>/',
         views.product_confirm_delete, name='product_confirm_delete')
]
