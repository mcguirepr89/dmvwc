# Generated by Django 5.0.2 on 2024-03-18 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calibers', '0004_caliber_inhouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='caliber',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]