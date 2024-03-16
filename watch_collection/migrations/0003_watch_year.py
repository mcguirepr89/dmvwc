# Generated by Django 5.0.2 on 2024-03-16 22:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_collection', '0002_alter_watch_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1800, message='Year must be greater than or equal to 1800.'), django.core.validators.MaxValueValidator(2024, message='Year must be less than or equal to the current year.')]),
        ),
    ]
