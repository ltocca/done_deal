from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Listing, Category
from .forms import NewListingForm, EditListingForm

# def all_listings


def detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    similar_listings = Listing.objects.filter(category=listing.category, is_sold=False).exclude(pk=pk)[0:3]
    near_listings = Listing.objects.filter(location=listing.location, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'listing/detail.html', {
        'listing': listing,
        'similar_listings': similar_listings,
        'near_listings': near_listings
    })


@login_required()
def new_listing(request):
    if request.method == 'POST':
        form = NewListingForm(request.POST, request.FILES)

        if form.is_valid():
            listing = form.save(commit=False)
            listing.seller = request.user
            # listing.image = form.cleaned_data['image']
            listing.save()

            return redirect('listing:detail', pk=listing.id)
    else:
        form = NewListingForm()

    return render(request, 'listing/new_listing.html', {
        'form': form,
        'title': 'New listing',
    })


@login_required
def edit_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk, seller=request.user)

    if request.method == 'POST':
        form = EditListingForm(request.POST, request.FILES, instance=listing)

        if form.is_valid():
            form.save()

            return redirect('listing:detail', pk=listing.id)
    else:
        form = EditListingForm(instance=listing)

    return render(request, 'listing/new_listing.html', {
        'form': form,
        'title': 'Edit listing',
    })


@login_required
def delete_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk, seller=request.user)
    listing.delete()

    return redirect('accounts:my_profile', pk=pk)
