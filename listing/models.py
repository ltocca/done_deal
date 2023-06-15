from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.name


class Listing(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(default="0")
    pub_date = models.DateField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)  # optional field
    category = models.ForeignKey(Category, related_name='listings', on_delete=models.CASCADE, blank=True, null=True)
    is_sold = models.BooleanField(default='False')
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='listings', on_delete=models.CASCADE)
    location = models.ForeignKey(Region, related_name='listings', on_delete=models.PROTECT, blank=True, null=True)
    image = models.ImageField(upload_to='listing_images', blank=True, null=True)


    def __str__(self):
        return self.title
