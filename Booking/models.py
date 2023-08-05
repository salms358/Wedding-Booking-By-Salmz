# models.py
from django.db import models
from .venue import Venue

class Location(models.Model):
    name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)


class Booking(models.Model):
    venue = models.ForeignKey(Location, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date = models.DateTimeField()
    table_count = models.PositiveIntegerField(default=1)
    cancelled = models.BooleanField(default=False)




