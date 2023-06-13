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


# def all_users(request):
#     if request.user.is_authenticated:
#         sort_param = request.GET.get('filter', 'name')  # Get the sorting parameter from the URL query string, defaulting to 'name'
#
#         if sort_param == 'name':
#             users = User.objects.all().order_by('name')
#         elif sort_param == '-name':
#             users = User.objects.all().order_by('-name')
#         elif sort_param == 'surname':
#             users = User.objects.all().order_by('surname')
#         elif sort_param == '-surname':
#             users = User.objects.all().order_by('-surname')
#         elif sort_param == 'year':
#             users = User.objects.all().order_by('date_of_birth')
#         elif sort_param == '-year':
#             users = User.objects.all().order_by('-date_of_birth')
#         else:
#             users = User.objects.all()
#
#         return render(request, 'accounts/all_users.html', {'users': users})
#     else:
#         return redirect('accounts:login')


def all_lisitngs(request):
    if request.user.is_authenticated:
        sort_param = request.GET.get('filter',
                                     'name')  # Get the sorting parameter from the URL query string, defaulting to 'name'

        if sort_param == 'name':
            artworks = Listing.objects.all().order_by('title')
        elif sort_param == '-name':
            artworks = Artwork.objects.all().order_by('-title')
        elif sort_param == 'year':
            artworks = Artwork.objects.all().order_by('year')
        elif sort_param == '-year':
            artworks = Artwork.objects.all().order_by('-year')
        elif sort_param == 'artist':
            artworks = Artwork.objects.all().order_by('artist')
        else:
            artworks = Artwork.objects.all()

        return render(request, 'artwork/all_artworks.html', {'artworks': artworks, 'sort_param': sort_param})
    else:
        return redirect('accounts:login')


def user_profile(request, pk):
    if request.user.is_authenticated:
        user = User.objects.get(pk=pk)
        my_artworks = artwork_models.Artwork.objects.filter(owner=pk)
        my_collections = artwork_models.Collection.objects.filter(owner=pk)
        collection_data = []
        for collection in my_collections:
            artworks_for_collection = artwork_models.Artwork.objects.filter(collection=collection)
            artworks_count = artworks_for_collection.count()
            collection_dict = {
                'collection': collection,
                'artworks': artworks_for_collection,
                'artworks_count': artworks_count,
            }
            collection_data.append(collection_dict)

        return render(request, 'accounts/profile.html',
                      {'user': user, 'my_artworks': my_artworks, 'my_collections': collection_data, 'pk': pk})
    else:
        return redirect('accounts:login')


def users_artworks(request, pk):
    if request.user.is_authenticated:
        sort_param = request.GET.get('filter',
                                     'name')  # Get the sorting parameter from the URL query string, defaulting to 'name'
        user = User.objects.get(pk=pk)
        if sort_param == 'name':
            artworks = artwork_models.Artwork.objects.filter(owner=pk).order_by('title')
        elif sort_param == '-name':
            artworks = artwork_models.Artwork.objects.filter(owner=pk).order_by('-title')
        elif sort_param == 'year':
            artworks = artwork_models.Artwork.objects.filter(owner=pk).order_by('year')
        elif sort_param == '-year':
            artworks = artwork_models.Artwork.objects.filter(owner=pk).order_by('-year')
        elif sort_param == 'artist':
            artworks = artwork_models.Artwork.objects.filter(owner=pk).order_by('artist')
        else:
            artworks = artwork_models.Artwork.objects.filter(owner=pk)

        return render(request, 'accounts/users_artworks.html', {
            'artworks': artworks,
            'user': user
        })
    else:
        return redirect('accounts:login')


def users_collections(request, pk):
    if request.user.is_authenticated:
        sort_param = request.GET.get('filter', 'name')
        if sort_param == 'name':
            collections = artwork_models.Collection.objects.filter(owner=pk).order_by('name')
        elif sort_param == '-name':
            collections = artwork_models.Collection.objects.filter(owner=pk).order_by('-name')
        else:
            collections = artwork_models.Collection.objects.filter(owner=pk)

        collection_data = []
        for collection in collections:
            artworks_for_collection = artwork_models.Artwork.objects.filter(collection=collection)
            artworks_count = artworks_for_collection.count()
            collection_dict = {
                'collection': collection,
                'artworks': artworks_for_collection,
                'artworks_count': artworks_count,
            }
            collection_data.append(collection_dict)

        return render(request, 'accounts/users_collections.html',
                      {'collections': collection_data, 'sort_param': sort_param})
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
    return render(request, 'accounts/change_password.html', {'form': form})
