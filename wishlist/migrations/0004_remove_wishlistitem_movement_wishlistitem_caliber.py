# Generated by Django 5.0.2 on 2024-03-16 20:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calibers', '0001_initial'),
        ('wishlist', '0003_alter_wishlistitem_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistitem',
            name='movement',
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='caliber',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calibers.caliber'),
        ),
    ]
