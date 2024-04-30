# Generated by Django 4.2.11 on 2024-04-30 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_remove_cart_user'),
        ('user', '0002_alter_profile_address_alter_profile_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cart',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.cart'),
        ),
    ]
