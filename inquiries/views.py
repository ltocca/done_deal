from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from listing.models import Listing

from .forms import InquiryMessageForm
from .models import Inquiry


@login_required
def new_chat(request, listing_pk):
    listing = get_object_or_404(Listing, pk=listing_pk)

    inquiries = Inquiry.objects.filter(listing=listing).filter(users__in=[request.user.id])

    if inquiries:
        return redirect('inquiry:chat', pk=inquiries.first().id)

    if request.method == 'POST':
        form = InquiryMessageForm(request.POST)

        if form.is_valid():
            inquiry = Inquiry.objects.create(listing=listing)
            inquiry.members.add(request.user)
            inquiry.members.add(listing.seller)
            inquiry.save()

            inquiry_message = form.save(commit=False)
            inquiry_message.inquiry = inquiry
            inquiry_message.created_by = request.user
            inquiry_message.save()

            return redirect('listing:chat', pk=listing_pk)
    else:
        form = InquiryMessageForm()

    return render(request, 'inquiry/new_chat', {
        'form': form
    })


@login_required
def inbox(request):
    inquiries = Inquiry.objects.filter(members__in=[request.user.id])

    return render(request, 'inquiry/inbox.html', {
        'inquiries': inquiries
    })


@login_required
def detail(request, pk):
    inquiry = Inquiry.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = InquiryMessageForm(request.POST)

        if form.is_valid():
            inquiry_message = form.save(commit=False)
            inquiry_message.inquiry = inquiry
            inquiry_message.created_by = request.user
            inquiry_message.save()

            inquiry.save()

            return redirect('inquiry:detail', pk=pk)
    else:
        form = InquiryMessageForm()

    return render(request, 'inquiry/detail.html', {
        'inquiry': inquiry,
        'form': form
    })