from django.db import models
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
    price = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                validators=[MinValueValidator(0.0)])
    category = models.CharField(
        max_length=255, choices=category_choices)
    description = models.TextField()

    img = models.ImageField(upload_to=get_image_upload_path, blank= True, null=True, default="images/default_image.png")

    def get_ratings_average(self):
        return self.product_ratings.all().aggregate(models.Avg("score", default=0))['score__avg']

    def __str__(self):
        s = '[' + str(self.name) + ' ' + str(self.price)
        return s


class Cart(models.Model):
    subtotal = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    shipping = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def add_product(self, cart_product):
        # Check if the product is already in the cart
        cp_id = cart_product.product.id
        func = (product for product in self.items.all()
                if product.product.id == cp_id)
        existing_product = next(func, None)
        if existing_product:
            existing_product.quantity += cart_product.quantity
            existing_product.subtotal += cart_product.subtotal
            existing_product.save()

        else:
            self.items.add(cart_product)
        self.recalculate()

    def remove_product(self, product_id):
        func = (cart_product for cart_product in self.items.all()
                if cart_product.id == product_id)
        product = next(func, None)
        product.delete()
        self.recalculate()

    def get_items(self):
        return self.items.all()

    def increase_quantity(self, cart_product_id):
        func = (cart_product for cart_product in self.items.all()
                if cart_product.id == cart_product_id)
        product = next(func, None)
        if product is not None:
            product.quantity += 1
            product.subtotal = product.product.price * product.quantity
            product.save()
            self.recalculate()
            return True
        return False

    def decrease_quantity(self, cart_product_id):
        func = (cart_product for cart_product in self.items.all()
                if cart_product.id == cart_product_id)
        product = next(func, None)
        if product.quantity == 1:
            product.delete()
        else:
            product.quantity -= 1
            product.subtotal = product.product.price * product.quantity
            product.save()
        self.recalculate()

    def recalculate(self):
        self.subtotal = 0
        for item in self.items.all():
            self.subtotal += item.subtotal
        self.shipping = 0 if self.subtotal >= 50 else 10
        self.total = self.subtotal + self.shipping
        self.save()

    def get_total_product_count(self):
        return sum([item.quantity for item in self.items.all()])

    def __str__(self):
        return '[ Cart id:' + str(self.id) + ' ]'


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items', null=True)

    def __str__(self):
        s = '[' + self.product.name + ' ' + str(self.quantity)
        s += ' ' + str(self.subtotal) + ']'
        return s
