
from django.urls import path
from . import views
from django.urls import include
from allauth.account.views import LoginView
from .views import update_booking, D_booking
app_name = 'Booking'
urlpatterns = [
    path('',views.index_view, name="index"),
    path('about_us/', views.about_us, name='about_us'),
    path('create_booking/', views.create_booking, name='create_booking'),
    path('view_booking/', views.view_booking, name='view_booking'),
    path('register/', views.register, name="register"),
    path('update_booking/<int:booking_id>/', update_booking.as_view(), name='update_booking'),
    path('delete_booking/<int:booking_id>/', D_booking.as_view(), name='delete_booking'),


]
