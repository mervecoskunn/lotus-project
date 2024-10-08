from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from shopping.models import Cart, Product
from user.models import Profile


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
    status = models.CharField(max_length=50, choices=status_choices, default=pending)
    created = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def create_order(cart, user_profile):
        order = Order(cart=cart, user_profile=user_profile)
        order.save()
        return order

    def __str__(self):
        return self.user_profile.user.username + ' - ' + self.status


class Rating(models.Model):
    rater = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_ratings')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='order_ratings')
    score = models.DecimalField(decimal_places=1, max_digits=3,
                                validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rater.username} - {self.product.name}"
