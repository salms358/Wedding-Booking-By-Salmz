from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Register, Booking
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, DeleteView


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
            return redirect('Booking:view_booking')
    else:
        booking_form = BookingForm()

    return render(request, 'create_booking.html', {'booking_form': booking_form})

@login_required
def view_booking(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request,'view_booking.html', {'bookings':bookings})

class update_booking(View):
    template_name = "update_booking.html"

    def get(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, pk=booking_id)
        form = BookingForm(instance=booking)
        return render(request,"update_booking.html",{'form': form, 'booking': booking})


    def post(self, request, *args, **kwargs):
            form = BookingForm(request.POST)
            if form.is_valid():
                user_profile = form.save(commit=False)
                user_profile.user = request.user  # Set the user for the profile
                user_profile.save()
            return render(request, 'update_booking.html', {'form': form})
            if form.is_valid():
                booking_date = form.cleaned_data.get('booking_date')

                if booking_date < timezone.now().date():
                    form.add_error('booking_date', 'Invalid date. Please select a future date.')
                else:
                    form.save()
                    return redirect('view_bookings')
        

class D_booking(DeleteView):
    model = Booking
    pk_url_kwarg = "booking_id"
    success_url = reverse_lazy("Booking:index")  # Redirect to the homepage
    template_name = "delete_booking.html"
    