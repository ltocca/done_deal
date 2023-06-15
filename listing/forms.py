# TODO: need toimplement some forms to edit a new listing

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
        fields = ('title', 'description', 'category', 'price', 'location', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Listing title'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Listing description'}),
            'category': forms.Select(attrs={'placeholder': 'Select category'}),
            'price': forms.TextInput(attrs={'placeholder': 'Set the listing price'}),
            'location': forms.Select(attrs={'placeholder': 'Select location'}),
            'image': forms.FileInput(attrs={'placeholder': 'Select photo'}),
        }


class EditListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'description', 'price', 'image', 'is_sold')