
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

    date_of_birth = forms.CharField(widget=forms.DateInput(attrs={
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


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'surname', 'date_of_birth', 'email', 'photo')

    widgets = {
        # 'photo': forms.FileInput(attrs={'placeholder': 'Select profile pic'}),
        'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        'name': forms.TextInput(attrs={'placeholder': 'Name'}),
        'surname': forms.TextInput(attrs={'placeholder': 'Surname'}), 'date_of_birth': forms.DateInput(
            attrs={'placeholder': 'Date of birth'}),
        'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        'photo': forms.FileInput(attrs={'placeholder': 'Photo'}),
    }



class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({
            'placeholder': 'Old password',
            'autocomplete': 'current-password',
        })
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={
            'placeholder': 'New password',
        })
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Repeat new password',
        })

    def clean_old_password(self):
        # Custom validation for the old password field
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError('The current password is incorrect.')
        return old_password
