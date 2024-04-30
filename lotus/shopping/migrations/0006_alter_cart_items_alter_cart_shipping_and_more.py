# Generated by Django 4.2.11 on 2024-04-30 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_remove_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(default=[], to='shopping.cartproduct'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='shipping',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
