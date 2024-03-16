# wishlist/admin.py

from django.contrib import admin
from .models import WishlistItem

@admin.register(WishlistItem)
class WatchlistItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'brand', 'model', 'caliber', 'example_photo', 'movement_photo', 'price', 'is_purchased']
