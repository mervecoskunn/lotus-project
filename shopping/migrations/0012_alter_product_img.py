# Generated by Django 4.2.11 on 2024-08-29 19:16

from django.db import migrations, models
import shopping.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0011_remove_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, default='https://www.contentviewspro.com/wp-content/uploads/2017/07/default_image.png', null=True, upload_to=shopping.models.get_image_upload_path),
        ),
    ]
