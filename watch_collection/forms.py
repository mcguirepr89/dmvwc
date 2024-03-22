# watch_collection/forms.py

from django import forms
from .models import Watch

class WatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = [
                'brand', 
                'model', 
                'year', 
                'caliber', 
                'example_photo', 
                'movement_photo', 
                'audio',
                'description',
                'price',
                'on_wishlist',
                ]

    on_wishlist = forms.BooleanField(
        widget=forms.Select(choices=[(True, 'In my collection'), (False, 'On my wishlist')]),
        required=False  # Set required=False if the field is not required
    )

class WatchDeleteForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = []

    watches_to_delete = forms.ModelMultipleChoiceField(
        queryset=Watch.objects.none(),
        widget=forms.CheckboxSelectMultiple,
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['watches_to_delete'].queryset = Watch.objects.filter(user=user)
