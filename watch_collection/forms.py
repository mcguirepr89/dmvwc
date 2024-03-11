# watch_collection/forms.py

from django import forms
from .models import Watch

class WatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = ['brand', 'model', 'movement', 'example_photo', 'movement_photo', 'audio']

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
