from django import forms
from .models import Booking
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Register
from django.utils import timezone
from datetime import timedelta


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
    ('Nawaabs Greenford', 'Nawaabs Greenford'),
    ('Slough Banqueting Hall', 'Slough Banqueting Hall'),
    ('Hounslow Banqueting Hall', 'Hounslow Banqueting Hall'),
]


class BookingForm(forms.ModelForm):
    venue = forms.ChoiceField(
        choices=VENUE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
        )
    booking_date = forms.DateField(
        label=_('Booking Date'),
        widget=forms.DateInput(attrs={'type': 'date'}),
        validators=[validate_date],
        )

    def clean_booking_date(self):
        booking_date = self.cleaned_data.get('booking_date')
        if booking_date < timezone.now().date():
            raise forms.ValidationError("Booking date cannot be in the past.")

        min_advance_booking_date = timezone.now().date() + timedelta(days=5)
        if booking_date < min_advance_booking_date:
            raise forms.ValidationError("Book at least 5 days in advance.")

        return booking_date

    def clean_booking_time(self):
        booking_time = self.cleaned_data.get('booking_time')
        if not datetime.time(14, 0) <= booking_time <= datetime.time(18, 0):
            raise forms.ValidationError("Booking are between 14:00 and 18:00.")

        return booking_time

    def group_capacity(self):
        group_size = self.cleaned_data.get("group_size")
        print(group_size)  # Add this line to check the value
        if group_size < 100 or group_size > 500:
            raise forms.ValidationError("Group size are between 100 and 500.")
        return group_size

    def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('booking_date')
        booking_time = cleaned_data.get('booking_time')

        # Check for existing bookings on the same date and time
        booking_to_update = self.instance
        existing_bookings = Booking.objects.filter(
            booking_date=booking_date,
            booking_time=booking_time
        )

        if existing_bookings.exists() and booking_to_update not in existing_bookings:
            raise forms.ValidationError('This date and time are already booked by another booking.')

        return cleaned_data

    class Meta:
        model = Booking
        fields = ['venue', 'customer_name', 'booking_date', 'booking_time', 'email', 'phone_number', 'theme', 'group_size']


class RegisteringAccount(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['user', 'first_name', 'last_name', 'phone_number']



        

