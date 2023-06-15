# TODO: need toimplement some forms to edit a new listing

from django import forms
from .models import Listing, Category, Region
from accounts.models import CustomUser as User


class NewListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'description', 'category', 'price', 'location', 'image')
        widgets = {
            'category': forms.Select(attrs={
                'placeholder': 'Category'
            }),
            'title': forms.TextInput(attrs={
                'placeholder': 'Listing Title'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Listing Description'
            }),
            'price': forms.TextInput(attrs={
                'placeholder': 'Price'
            }),
            'location': forms.Select(attrs={
                'placeholder': 'Listing location'
            }),
            'image': forms.FileInput(attrs={
                'placeholder': 'Listing Photo'
            })
        }


class EditListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'description', 'price', 'image', 'is_sold')


        # TODO: fix no upload image