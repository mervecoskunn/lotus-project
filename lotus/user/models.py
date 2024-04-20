from django.db import models
from shopping.models import product_list

# Create your models here.


class User:
    def __init__(self, username, email, password, favorites=[]):
        self.username = username
        self.email = email
        self.password = password
        self.favorites = favorites

    def add_to_favorites(self, product):
        self.favorites.append(product)

    def remove_from_favorites(self, id):
        self.favorites = [
            product for product in self.favorites if product.id != id]

    def __str__(self):
        return self.username


user1 = User("user1", "", "", [product_list[0],
             product_list[1], product_list[2]])
user2 = User("user2", "", "", [])
user3 = User("user3", "", "", [])
