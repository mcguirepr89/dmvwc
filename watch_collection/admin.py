# watch_collection/admin.py

from django.contrib import admin
from .models import Watch

@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ['user', 'brand', 'model', 'caliber', 'example_photo', 'movement_photo', 'audio']
