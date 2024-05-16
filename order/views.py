from django.shortcuts import render, redirect
import stripe
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from shopping.models import Cart
from order.models import Order
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings


@login_required
def orders(request):
    user_profile = request.user.profile
    orders = user_profile.orders.all()
    return render(request, 'order/orders.html', {'orders': orders})


@login_required
def all_orders(request):
    orders = Order.objects.all()
    return render(request, 'order/orders.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order/order_detail.html', {'order': order})


@login_required
def edit_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        order.status = status
        order.save()
        messages.success(request, 'Order status updated successfully.')
        return redirect('orders')
    return render(request, 'order/edit_order.html', {'order': order})


@login_required
def success(request):
    user_profile = request.user.profile
    order = Order.create_order(user_profile.cart, user_profile)

    user_profile.create_new_cart()
    user = user_profile.user
    # Send email to user
    html_content = render_to_string(
        template_name="order/order_email.html",
        context={
            'user': user.username,
            'domain': get_current_site(request).domain,
            "protocol": "https" if request.is_secure() else "http",
            "order_id": order.id,
        }
    )
    plain_message = strip_tags(html_content)

    send_mail(
        subject='Order Confirmation',
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_content,
        fail_silently=True
    )

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
