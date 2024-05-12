from django.urls import path
import order.views as order_views


urlpatterns = [
    path('create-checkout-session/',
         order_views.create_checkout_session, name='create_checkout_session'),
    path('success/', order_views.success, name='success'),
    path('cancel/', order_views.cancel, name='cancel'),
    path('orders/', order_views.orders, name='orders'),
    path('order_detail/<int:order_id>/',
         order_views.order_detail, name='order_detail'),
    path('edit_order/<int:order_id>/', order_views.edit_order, name='edit_order')
]
