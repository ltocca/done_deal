from django.conf import settings
from django.db import models
from listing.models import Listing
from django.contrib.auth.models import User


class Inquiry(models.Model):
    listing = models.ForeignKey(Listing, related_name='inquiries', on_delete=models.CASCADE)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='inquiries')
    started_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-modified_at',)


class InquiryMessage(models.Model):
    approach = models.ForeignKey(Inquiry, related_name='approach', on_delete=models.CASCADE)
    msg = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    sent_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sender', on_delete=models.CASCADE)
