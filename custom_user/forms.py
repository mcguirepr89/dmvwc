# custom_user/forms.py

from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'border border-2 w-full rounded-md shadow-lg p-2'
        self.fields['first_name'].widget.attrs['class'] = 'border border-2 w-full rounded-md shadow-lg p-2'
        self.fields['last_name'].widget.attrs['class'] = 'border border-2 w-full rounded-md shadow-lg p-2'
        self.fields['email'].widget.attrs['class'] = 'border border-2 w-full rounded-md shadow-lg p-2'
        self.fields['watch_collection_visibility'].widget.attrs['class'] = 'border border-2 w-full rounded-md shadow-lg p-2'
        self.fields['wishlist_visibility'].widget.attrs['class'] = 'border border-2 w-full rounded-md shadow-lg p-2'

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'watch_collection_visibility', 'wishlist_visibility']  # Add all fields you want to include
