# Generated by Django 5.0.2 on 2024-03-17 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0006_merge_20240317_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistitem',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
