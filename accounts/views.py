from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import SignupForm, LoginForm, EditProfileForm, ChangePasswordForm
from .models import CustomUser as User
from listing import models as listing_models
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')

# TODO: implementare viste