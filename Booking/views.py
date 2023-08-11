from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Register, Booking


class RegisterView(View):
    template_name = "register.html"

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                messages.success(request, 'Account created successfully!')
                return redirect('Booking:index')
            except IntegrityError:
                messages.error(request, 'An account with these details already exists.')
        return render(request, self.template_name, {'form': form})

class CreateProfileView(View):
    template_name = "create_profile.html"

    def get(self, request, *args, **kwargs):
        form = BookingForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """
        Post method for creating profile
        """
        form = BookingForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user 
            user_profile.save()
            return redirect('index')  
            return render(request, self.template_name, {'form': form})
        
def index_view(request):
    return render(request, 'base.html')

def about_us(request):
    return render(request, 'about_us.html')

def register(request):
    return render(request, 'register.html')
def account_login(request):
    return render(request, 'login.html')


# CRUD functionality
def create_booking(request):
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            # Save the booking object with the user
            booking.user = request.user
            booking.save()
            return redirect('Booking:view_booking')  # Correct view name here
    else:
        booking_form = BookingForm()

    return render(request, 'create_booking.html', {'booking_form': booking_form})

@login_required
def view_booking(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'Booking:view_booking') 

class EditBookingView(View):
    template_name = "edit_booking.html"

    def get(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, pk=booking_id)
        form = BookingForm(instance=booking)
        return render(request, self.template_name, {'form': form, 'booking': booking})


def post(self, request, *args, **kwargs):
        form = BookingFormForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user  # Set the user for the profile
            user_profile.save()
            return redirect('home')  # Replace 'home' with the name of your home view
        return render(request, self.template_name, {'form': form})


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking.delete()
        return redirect('index')
    
    return render(request, 'delete_booking.html', {'booking': booking})
