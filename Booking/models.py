# models.py
from django.db import models
from .venue import Venue
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)


class Booking(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    booking_date = models.DateField(auto_now=False)
    booking_time = models.TimeField(auto_now=False)
    phone_number = models.CharField(max_length=20)
    theme = models.CharField(max_length=100, blank=True)
    # Other fields of the Booking model
class Register(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=11)




