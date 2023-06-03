from django.contrib import admin

# Register your models here.

from real_estates.models import RealEstates, Links

admin.site.register(RealEstates)
admin.site.register(Links)

