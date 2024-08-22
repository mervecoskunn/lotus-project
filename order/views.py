from django.db.models import Avg
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import stripe
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.urls import reverse

from shopping.models import Cart, Product, CartProduct
from order.models import Order, Rating
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


@login_required
def orders(request):
    user_profile = request.user.profile
    orders = user_profile.orders.all()
    return render(request, 'order/orders.html', {
        'orders': orders, 'prev_page': 'orders'
    })


@login_required
def all_orders(request):
    orders = Order.objects.all()
    return render(request, 'order/orders.html', {
        'orders': orders, 'prev_page': 'all_orders'
    })


@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    prev_page = request.META.get('HTTP_REFERER', '/')
    return render(request, 'order/order_detail.html', {
        'order': order, 'prev_page': prev_page
    })


@login_required
def my_assessments(request):
    prev_page = request.META.get('HTTP_REFERER', '/')

    if request.method == 'GET':
        ratings = Rating.objects.filter(rater=request.user).values_list('product__id', flat=True)
        queryset = CartProduct.objects.exclude(product__id__in=ratings).filter(
            cart__order__user_profile__user=request.user
        )
        data = []
        product_ids = []

        for cp in queryset:
            if cp.product.id not in product_ids:
                product_ids.append(cp.product.id)
                rate = Rating.objects.filter(product=cp.product)

                context = {
                    "product_id": cp.product.id,
                    "product_name": cp.product.name,
                    "product_img": cp.product.img,
                    "rating_average": rate.aggregate(Avg("score", default=0))['score__avg'],
                    "rating_count": rate.count()
                }
                data.append(context)

        return render(request, 'order/my_assessment.html', {
            'products': data, 'prev_page': prev_page
        })

    elif request.method == 'POST':
        product_id = request.POST.get('productId')
        score = request.POST.get('rating')
        comment = request.POST.get('review')
        product = Product.objects.get(id=product_id)

        Rating.objects.create(rater=request.user, product=product, score=score, comment=comment)
        return HttpResponseRedirect(reverse('my_assessment'))


@login_required
def edit_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        prev_page = request.POST.get('prev_page')
        order.status = status
        order.save()
        messages.success(request, 'Order status updated successfully.')
        return redirect(prev_page)


@login_required
def success(request):
    send_order_email(request)
    return render(request, 'order/success.html')


@login_required
def cancel(request):
    return render(request, 'order/cancel.html')


@login_required
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    protocol = "https" if request.is_secure() else "http"
    DOMAIN = protocol + '://' + get_current_site(request).domain

    cart_id = request.POST.get('cart_id')
    cart = Cart.objects.get(id=cart_id)
    total_price = int(cart.total * 100)
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
        success_url=DOMAIN + '/order/success',
        cancel_url=DOMAIN + '/order/cancel',
    )

    return redirect(checkout_session.url, code=303)


def send_order_email(request):
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


def send_order_not_confirmed_email(request):
    user = request.user
    # Send email to user
    html_content = render_to_string(
        template_name="order/order_not_confirmed_email.html",
        context={
            'user': user.username,
            'domain': get_current_site(request).domain,
            "protocol": "https" if request.is_secure() else "http",
        }
    )
    plain_message = strip_tags(html_content)

    send_mail(
        subject='Order Not Confirmed',
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_content,
        fail_silently=True
    )


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    print("Webhook payload: ", payload)

    # Passed signature verification
    return HttpResponse(status=200)
