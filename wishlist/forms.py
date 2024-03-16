# wishlist/forms.py

from django import forms
from .models import WishlistItem

class WishlistItemForm(forms.ModelForm):
    class Meta:
        model = WishlistItem
        fields = ['brand', 'model', 'year', 'caliber', 'example_photo', 'movement_photo', 'description', 'price', 'is_purchased']

class WishlistItemDeleteForm(forms.ModelForm):
    class Meta:
        model = WishlistItem
        fields = []

    items_to_delete = forms.ModelMultipleChoiceField(
        queryset=WishlistItem.objects.none(),
        widget=forms.CheckboxSelectMultiple,
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['items_to_delete'].queryset = WishlistItem.objects.filter(user=user)
