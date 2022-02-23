from django.contrib import admin

# Register your models here.
from hotel_data.models import Hotel, City

admin.site.register(Hotel)
admin.site.register(City)