from django.db import models
from shopping.models import Cart
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True, blank=True)
    favorites = models.ManyToManyField('shopping.Product', blank=True)
    cart = models.OneToOneField(
        Cart, on_delete=models.CASCADE, null=True)

    def add_to_favorites(self, product):
        self.favorites.add(product)

    def remove_from_favorites(self, id):
        product = self.favorites.get(id=id)
        self.favorites.remove(product)

    def create_new_cart(self):
        cart = Cart()
        cart.save()
        self.cart = cart
        self.save()

    def __str__(self):
        return self.user.username
