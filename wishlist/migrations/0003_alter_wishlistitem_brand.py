# Generated by Django 5.0.2 on 2024-03-16 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0004_alter_brand_options'),
        ('wishlist', '0002_alter_wishlistitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistitem',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.brand'),
        ),
    ]
