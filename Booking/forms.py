
from django import forms
from .models import Booking
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Register

def validate_date(date):
    if not date:
        raise ValidationError(
            _('This field is required.'),
            code='required'
        )

    try:
        # Attempt to parse the date
        # If successful, it's a valid date
        datetime.datetime.strptime(str(date), '%Y-%m-%d')
    except ValueError:
        raise ValidationError(
            _('Enter a valid date.'),
            code='invalid_date'
        )

VENUE_CHOICES = [
    ('Venue1', 'Nawaabs Greenford'),
    ('Venue2', 'Slough Banqueting Hall'),
    ('Venue3', 'Hounslow Banqueting Hall'),
]

class BookingForm(forms.ModelForm):
    venue = forms.ChoiceField(choices=VENUE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    booking_date = forms.DateField(
        label=_('Booking Date'),
        widget=forms.DateInput(attrs={'type': 'date'}),
        validators=[validate_date],
    )

    class Meta:
        model = Booking
        fields = ['venue', 'customer_name', 'booking_date', 'booking_time', 'email', 'phone_number', 'theme']


class RegisteringAccount(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['user', 'first_name', 'last_name', 'phone_number']



        

