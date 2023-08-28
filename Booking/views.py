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
from allauth.account.views import LogoutView, PasswordResetView
from .email_utils import send_verification_email, send_custom_email
from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation
from django.http import JsonResponse
from django.utils import timezone


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
        
class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "index.html",
            {
                "home_active": "custom-red",
            }
        )


def about_us(request):
    return render(request, 'about_us.html')

def register(request):
    return render(request, 'register.html')
def account_login(request):
    return render(request, 'login.html')
class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'


# CRUD functionality
@ login_required
def create_booking(request):
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            # Save the booking object with the user
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking successfully created')
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
        if booking.user.id != self.request.user.id:
            return redirect('/')
            
        form = BookingForm(instance=booking)
        return render(request,"update_booking.html",{'form': form, 'booking': booking})


    def post(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, pk=booking_id)
        if (booking.user != self.request.user) and (not self.request.user.is_superuser):
            messages.error(request, 'You do not have permission to update this booking.')
            return redirect('Booking:view_booking')

        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking_date = form.cleaned_data.get('booking_date')

            if booking_date < timezone.now().date():
                form.add_error('booking_date', 'Invalid date. Please select a future date.')
            else:
                form.save()
                messages.success(request, 'Booking successfully updated')
                return redirect('Booking:view_booking')
        else:
            messages.error(request, 'Failed to update booking. Please check your input.')

        return render(request, 'update_booking.html', {'form': form, 'booking': booking})

class D_booking(DeleteView):
    model = Booking
    pk_url_kwarg = "booking_id"
    success_url = reverse_lazy("Booking:index")  # Redirect to the homepage
    template_name = "delete_booking.html"

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Booking deleted successfully.')  
        return super().delete(request, *args, **kwargs)


class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Send reset password email using EmailJS
        template_params = {
            "to_email": form.cleaned_data["email"],
            "user_id": "your_user_id",  # Replace with your EmailJS user ID
            "template_id": "your_template_id",  # Replace with your EmailJS template ID
            "email_params": {
                "reset_link": response.context_data["reset_url"],
            },
        }
        emailjs.send("service_h4d0j1w", "your_emailjs_template_id", template_params);

        return JsonResponse({"message": "Password reset email sent."})


def some_view(request):
    # ...
    send_verification_email(request, user)
def send_verification_email(request, user):
    email_address = EmailAddress.objects.get(user=user, primary=True)
