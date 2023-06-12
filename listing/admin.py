from django.contrib import admin

from .models import Category
from .models import Region
from .models import Listing
from .models import User

admin.site.register(Category)
admin.site.register(Region)
admin.site.register(Listing)
admin.site.register(User)
