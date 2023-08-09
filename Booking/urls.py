
from django.urls import path
from . import views
from django.urls import include
from allauth.account.views import LoginView
app_name = 'Booking'
urlpatterns = [
    path('',views.index_view, name="index"),
    path('about_us/', views.about_us, name='about_us'),
    path('create_booking/', views.create_booking, name='create_booking'),
    path('register/', views.register, name="register")

   
    

 

]
