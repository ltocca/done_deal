from django.shortcuts import render
from listing.models import *


def index(request):
    listings = Listing.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'listings': listings,
    })


def contacts(request):
    return render(request, 'core/contacts.html')
