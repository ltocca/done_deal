from django.shortcuts import render, get_object_or_404

from listing.models import Listing


def detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)

    return render(request, 'listing/detail.html', {
        'listing': listing
    })
