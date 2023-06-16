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
            inquiry.users.add(request.user)
            inquiry.users.add(listing.seller)
            inquiry.save()

            inquiry_message = form.save(commit=False)
            inquiry_message.approach = inquiry
            inquiry_message.sent_by = request.user
            inquiry_message.save()

            return redirect('listing:detail', pk=listing_pk)
    else:
        form = InquiryMessageForm()

    return render(request, 'inquiries/new_chat.html', {
        'form': form
    })


@login_required
def inbox(request):
    inquiries = Inquiry.objects.filter(users__in=[request.user.id])

    return render(request, 'inquiries/inbox.html', {
        'inquiries': inquiries
    })


@login_required
def chat(request, pk):
    inquiry = Inquiry.objects.filter(users__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = InquiryMessageForm(request.POST)

        if form.is_valid():
            inquiry_message = form.save(commit=False)
            inquiry_message.approach = inquiry
            inquiry_message.sent_by = request.user
            inquiry_message.save()

            inquiry.save()

            return redirect('inquiry:chat', pk=pk)
    else:
        form = InquiryMessageForm()

    return render(request, 'inquiries/chat.html', {
        'inquiry': inquiry,
        'form': form
    })
