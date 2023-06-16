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


def user_profile(request, pk):
    if request.user.is_authenticated:
        user = User.objects.get(pk=pk)
        my_listings = listing_models.Listing.objects.filter(seller=pk)

        return render(request, 'accounts/my_profile.html',
                      {'user': user, 'my_listings': my_listings, 'pk': pk})
    else:
        return redirect('accounts:login')


@login_required
def edit_profile(request, pk):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.photo = form.cleaned_data['photo']
            form.save()
            return redirect('accounts:my_profile', pk=pk)
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password has been changed successfully.')
            return redirect('accounts:my_profile', pk=request.user.pk)
    else:
        form = ChangePasswordForm(request.user)
        messages.error(request, 'Your password has not changed. Check again')
    return render(request, 'accounts/change_password.html', {'form': form})
