# watch_collection/admin.py

from django.contrib import admin
from .models import Watch
from .forms import WatchForm

@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    form = WatchForm
