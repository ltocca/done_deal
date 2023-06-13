from django.shortcuts import render, get_object_or_404

from listing.models import Listing


def detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    similar_listings = Listing.objects.filter(category=listing.category, is_sold=False).exclude(pk=pk)[0:3]
    near_lisitngs = Listing.objects.filter(location=listing.location, is_sold=False).exclude(pk=pk)[0:3]


    return render(request, 'listing/detail.html', {
        'listing': listing
    })
