# Generated by Django 4.2.11 on 2024-05-20 05:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0009_remove_cart_items_cartproduct_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
