
from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_venue, name='book_venue'),
    path('booking_list/', views.booking_list, name='booking_list'),
    # Add other URLs as needed
]
