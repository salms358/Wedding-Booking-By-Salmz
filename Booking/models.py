from django.db import models
from django.contrib.auth.models import User
from .venue import Venue
from django.core.validators import MinValueValidator, MaxValueValidator

"""
The database models for the booking form and the registration one is not used
"""
class Booking(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE, primary_key=True)
    venue = models.CharField(max_length=100, blank=False)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    booking_date = models.DateField(auto_now=False)
    booking_time = models.TimeField(auto_now=False)
    phone_number = models.CharField(max_length=20)
    theme = models.CharField(max_length=100, blank=True)
    group_size = models.PositiveIntegerField(default=100, 
    validators=[MinValueValidator(100), MaxValueValidator(500)])
   


class Register(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=11)
