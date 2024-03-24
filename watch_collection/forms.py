# watch_collection/forms.py

from django import forms
from .models import Watch, Caliber

class BooleanDropdown(forms.TypedChoiceField):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            coerce=lambda x: x == 'True',
            choices=((False, 'In my collection'), (True, 'On my wishlist')),
            **kwargs
        )

class WatchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand'].widget.attrs['class'] = 'border border-2 w-full rounded-md shadow-lg'
        self.fields['model'].widget.attrs['class'] = 'border border-2 w-full rounded-md shadow-lg'
        self.fields['year'].widget.attrs['class'] = 'border border-2 rounded-md shadow-lg'
        self.fields['example_photo'].widget.attrs['class'] = 'border border-2 rounded-md shadow-lg'
        self.fields['movement_photo'].widget.attrs['class'] = 'border border-2 rounded-md shadow-lg'
        self.fields['audio'].widget.attrs['class'] = 'border border-2 rounded-md shadow-lg'
        # Add the initial choice for caliber selection
        calibers = Caliber.objects.all()
        choices = [('', 'Choose from the list below')]
        choices += [('1', 'Add a new caliber')]
        choices += [('', '-----------------')]
        choices += [(caliber.id, caliber.name) for caliber in calibers]
        self.fields['caliber'].choices = choices
        self.fields['caliber'].widget.attrs['class'] = 'border border-2 w-full rounded-md shadow-lg'
        self.fields['description'].widget.attrs['class'] = 'border border-2 w-full rounded-md shadow-lg'
        self.fields['price'].widget.attrs['class'] = 'border border-2 rounded-md shadow-lg'
        self.fields['on_wishlist'] = BooleanDropdown()
        self.fields['on_wishlist'].widget.attrs['class'] = 'border border-2 rounded-md shadow-lg'

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
