from django.shortcuts import render, redirect
from django.views import View
import stripe
from django.conf import settings
from django.http import JsonResponse

from shopping.models import Cart
from order.models import Order
from django.contrib.auth.decorators import login_required


def orders(request):
    user_profile = request.user.profile
    orders = user_profile.orders.all()
    return render(request, 'order/orders.html', {'orders': orders})


@login_required
def success(request):
    user_profile = request.user.profile
    Order.create_order(user_profile.cart, user_profile)

    user_profile.create_new_cart()

    return render(request, 'order/success.html')


@login_required
def cancel(request):
    return render(request, 'order/cancel.html')


@login_required
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    YOUR_DOMAIN = 'http://127.0.0.1:8000'

    cart_id = request.POST.get('cart_id')
    cart = Cart.objects.get(id=cart_id)
    total_price = int(cart.total * 100)
    print(cart)
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'eur',
                    'unit_amount': total_price,
                    'product_data': {
                        'name': 'Cart Total',
                    },

                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=YOUR_DOMAIN + '/order/success',
        cancel_url=YOUR_DOMAIN + '/order/cancel',
    )

    return redirect(checkout_session.url, code=303)


# class CreateCheckoutSessionView(View):
#     def post(self, request, *args, **kwargs):
#         cart_id = self.kwargs['cart_id']
#         cart = Cart.objects.get(id=cart_id)

#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[
#                 {
#                     # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
#                     'price': '{{PRICE_ID}}',
#                     'quantity': 1,
#                 },
#             ],
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/success',
#             cancel_url=YOUR_DOMAIN + '/cancel',
#         )

#         return JsonResponse({
#             'id': checkout_session.id
#         })
