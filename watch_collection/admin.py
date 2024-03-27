# watch_collection/admin.py

from django.contrib import admin
from .models import Watch
from .forms import WatchForm

@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ('user', 'brand', 'year', 'model', 'caliber', 
                    'example_photo', 'movement_photo', 'audio', 'price',
                    'on_wishlist', 'created_at')
    #form = WatchForm
