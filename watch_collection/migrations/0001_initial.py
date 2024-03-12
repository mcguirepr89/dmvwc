# Generated by Django 5.0.2 on 2024-03-05 19:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
                ('movement', models.CharField(max_length=100)),
                ('example_photo', models.ImageField(blank=True, null=True, upload_to='watch_example_photos/')),
                ('movement_photo', models.ImageField(blank=True, null=True, upload_to='watch_movement_photos/')),
                ('audio', models.FileField(blank=True, null=True, upload_to='watch_audio/')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Watches',
            },
        ),
    ]
