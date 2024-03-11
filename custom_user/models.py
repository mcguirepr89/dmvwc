from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # You can add any additional fields or customization here if needed.
    editability = models.BooleanField(default=False)
    
    # New fields for visibility settings
    WATCH_COLLECTION_VISIBILITY_CHOICES = [
        ('public', 'Public'),
        ('logged_in_users', 'Logged In Users Only'),
        ('private', 'Private'),
    ]
    watch_collection_visibility = models.CharField(
        max_length=20,
        choices=WATCH_COLLECTION_VISIBILITY_CHOICES,
        default='private',  # Default to private for existing users
    )

    WISHLIST_VISIBILITY_CHOICES = [
        ('public', 'Public'),
        ('logged_in_users', 'Logged In Users Only'),
        ('private', 'Private'),
    ]
    wishlist_visibility = models.CharField(
        max_length=20,
        choices=WISHLIST_VISIBILITY_CHOICES,
        default='private',  # Default to private for existing users
    )

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Club Members'
