# Generated by Django 5.0.2 on 2024-03-16 20:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calibers', '0001_initial'),
        ('watch_collection', '0002_alter_watch_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watch',
            name='movement',
        ),
        migrations.AddField(
            model_name='watch',
            name='caliber',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calibers.caliber'),
        ),
    ]
