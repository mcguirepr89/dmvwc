# wishlist/models.py

from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from custom_user.models import CustomUser
import os

class WishlistItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100, null=True, blank=True)
    movement = models.CharField(max_length=100, null=True, blank=True)
    example_photo = models.ImageField(upload_to='watch_example_photos/', null=True, blank=True)
    movement_photo = models.ImageField(upload_to='watch_movement_photos/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_purchased = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.brand} - {self.model} - {self.movement}'

# Signal to delete associated image files when a WishlistItem instance is deleted
@receiver(pre_delete, sender=WishlistItem)
def wishlist_item_pre_delete(sender, instance, **kwargs):
    # Delete example_photo
    if instance.example_photo:
        if os.path.isfile(instance.example_photo.path):
            os.remove(instance.example_photo.path)

    # Delete movement_photo
    if instance.movement_photo:
        if os.path.isfile(instance.movement_photo.path):
            os.remove(instance.movement_photo.path)

