from django.contrib import admin
from .models import Brand

class BrandAdmin(admin.ModelAdmin):
    # Add any other customization options here
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ['name']

admin.site.register(Brand, BrandAdmin)
