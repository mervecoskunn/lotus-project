from django.db import models
from shopping.models import Cart
from user.models import Profile

# Create your models here.


class Order(models.Model):
    pending = 'Pending'
    delivered = 'Delivered'
    cancelled = 'Cancelled'
    status_choices = [
        (pending, 'Pending'),
        (delivered, 'Delivered'),
        (cancelled, 'Cancelled')
    ]

    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(
        max_length=50, choices=status_choices, default=pending)
    created = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def create_order(cart, user_profile):
        order = Order(cart=cart, user_profile=user_profile)
        order.save()
        return order

    def __str__(self):
        return self.user_profile.user.username + ' - ' + self.status
