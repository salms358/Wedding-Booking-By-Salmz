# models.py
from django.db import models
from .venue import Venue

class Location(models.Model):
    name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)


class Booking(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    date = models.DateField()
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    # Other fields of the Booking model





