from django.contrib import admin
# Import Booking model from models.py
from .models import Booking

@admin.register(Booking)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'email','phone_number','date','table_count','cancelled')
    search_fields = ('customer_name','venue')
    list_filter = ('venue', 'phone_number')


