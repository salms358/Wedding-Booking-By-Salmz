
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['venue', 'customer_name', 'email', 'phone_number','date']


        

