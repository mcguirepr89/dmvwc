# Generated by Django 5.0.2 on 2024-03-16 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_collection', '0003_watch_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch',
            name='movement',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]