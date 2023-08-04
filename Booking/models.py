# models.py
from django.db import models
from .venue import Venue

class Booking(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date_time = models.DateTimeField()
    table_count = models.PositiveIntegerField(default=1)
    is_canceled = models.BooleanField(default=False)

class Menu(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    appetizer = models.CharField(max_length=100)
    main_course = models.CharField(max_length=100)
    dessert = models.CharField(max_length=100)


