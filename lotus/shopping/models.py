from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


cat_bracelet = 'bracelet'
cat_chackra_stone = 'chakra_stone'
cat_incense = 'incence'
cat_natural_stone = 'natural_stone'
cat_pendulum = 'pendulum'
cat_none = "none"


def get_category_suffix(category):
    return str(category).replace(' ', '_').lower()


def get_image_upload_path(instance, filename):
    # Define the directory structure based on the category
    return f'products/{get_category_suffix(instance.category)}/{filename}'


class Product(models.Model):
    category_choices = (
        (cat_bracelet, 'Bracelet'),
        (cat_chackra_stone, 'Chakra Stone'),
        (cat_incense, 'Incense'),
        (cat_natural_stone, 'Natural Stone'),
        (cat_pendulum, 'Pendulum'),
        (cat_none, 'None')
    )

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(
        max_length=255, choices=category_choices)
    description = models.TextField()
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    img = models.ImageField(upload_to=get_image_upload_path, null=True)

    def __str__(self):
        return '[' + self.name + ' ' + str(self.price) + ' ' + str(self.rating) + ']'


class Cart(models.Model):
    subtotal = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    shipping = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def add_product(self, cart_product):
        # Check if the product is already in the cart
        existing_product = next(
            (product for product in self.items.all() if product.product.id == cart_product.product.id), None)
        if existing_product:
            existing_product.quantity += cart_product.quantity
            existing_product.subtotal += cart_product.subtotal
            existing_product.save()

        else:
            self.items.add(cart_product)
        self.subtotal += cart_product.subtotal
        self.shipping = 0 if self.subtotal > 150 else 10
        self.total = self.subtotal + self.shipping
        self.save()

    def remove_product(self, product_id):
        product = next(
            (cart_product for cart_product in self.items if cart_product.product.id == product_id), None)
        self.items.remove(product)
        self.subtotal -= product.subtotal
        self.shipping = 0 if self.subtotal > 150 else 10
        self.total = self.subtotal + self.shipping
        self.save()

    def get_items(self):
        return self.items.all()

    def __str__(self):
        return '[ Cart id:' + str(self.id) + ' ]'


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items', null=True)

    def __str__(self):
        return '[' + str(self.product.name) + ' ' + str(self.quantity) + ' ' + str(self.subtotal) + ']'
