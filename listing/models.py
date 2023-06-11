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


class Listing(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)  # optional field
    price = models.FloatField()
    is_sold = models.BooleanField()
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='listings', on_delete=models.CASCADE)
    # TODO: Regione
