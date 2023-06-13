#TODO: need to implement SignupForm, LoginForm, EditProfileForm, ChangePasswordForm

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'surname', 'date_of_birth', 'email', 'password1', 'password2')


class LoginForm:
    pass


class EditProfileForm:
    pass


class ChangePasswordForm:
    pass