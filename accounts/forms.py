# TODO: need to implement EditProfileForm, ChangePasswordForm

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import CustomUser


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'surname', 'date_of_birth', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username'
    }))

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Name'
    }))

    surname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last name'
    }))

    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(attrs={
        'placeholder': 'Your birthday'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email'
    }))

    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    #     'placeholder': 'Password'
    # }))
    #
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    #     'placeholder': 'Confirm password'
    # }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))


class EditProfileForm:
    pass


class ChangePasswordForm:
    pass
