# custom_user/forms.py

from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'watch_collection_visibility', 'wishlist_visibility', ]  # Add all fields you want to include
