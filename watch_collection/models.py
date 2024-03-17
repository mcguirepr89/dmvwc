# watch_collection/models.py

from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from custom_user.models import CustomUser
from brands.models import Brand
from calibers.models import Caliber
import os
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

class Watch(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    YEAR_CHOICES = [(year, str(year)) for year in range(1800, datetime.now().year + 1)]
    year = models.IntegerField(choices=YEAR_CHOICES[::-1], null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    caliber = models.ForeignKey(Caliber, on_delete=models.CASCADE, null=True, blank=True)
    example_photo = models.ImageField(upload_to='watch_example_photos/', null=True, blank=True)
    movement_photo = models.ImageField(upload_to='watch_movement_photos/', null=True, blank=True)
    audio = models.FileField(upload_to='watch_audio/', null=True, blank=True)

    def __str__(self):
        return f'{self.brand} - {self.model} - {self.movement}'

    class Meta:
        verbose_name_plural = 'Watches'

# Signal to delete associated image files when a Watch instance is deleted
@receiver(pre_delete, sender=Watch)
def watch_pre_delete(sender, instance, **kwargs):
    # Delete example_photo
    if instance.example_photo:
        if os.path.isfile(instance.example_photo.path):
            os.remove(instance.example_photo.path)

    # Delete movement_photo
    if instance.movement_photo:
        if os.path.isfile(instance.movement_photo.path):
            os.remove(instance.movement_photo.path)

    # Delete audio file
    if instance.audio:
        if os.path.isfile(instance.audio.path):
            os.remove(instance.audio.path)

