# TODO: need toimplement some forms to add a new listing and to edit it

from django import forms
from .models import Listing, Category, Region
from accounts.models import CustomUser as User

class NewListingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['listings'].queryset = Listing.objects.filter(seller=user)

    class Meta:
        model = Listing
        fields = ['artist', 'genre', 'title', 'description', 'collection', 'year', 'photo']
        widgets = {
            'artist': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Artist'}),
            'genre': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Genre'}),
            'title': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Artwork title'}),
            'description': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Artwork description'}),
            'year': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Artwork year'}),
            'collection': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Collection'}),
            'photo': forms.FileInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Artwork photo'}),
        }