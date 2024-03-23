# calibers/forms.py

from django import forms
from .models import Caliber

class CaliberForm(forms.ModelForm):
    class Meta:
        model = Caliber
        fields = ['name', 'type', 'inhouse']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'border border-2 p-2 rounded-md'
        self.fields['type'].widget.attrs['class'] = 'border border-2 p-2 rounded-md'
        self.fields['inhouse'].widget.attrs['class'] = 'border border-2 p-2 rounded-md'
