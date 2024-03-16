from django.contrib import admin
from .models import Caliber

class CaliberAdmin(admin.ModelAdmin):
    # Add any other customization options here
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ['name']

admin.site.register(Caliber, CaliberAdmin)
