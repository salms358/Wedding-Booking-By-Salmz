from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .forms import BookingForm
from .models import Register

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

class CreateProfile(View):
    template_name = "create_profile.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request):
        f_name = request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        tele = request.POST.get("phone_number")

        CreateUserProfile = UserProfile.objects.create(
            first_name=f_name,
            last_name=l_name,
            phone_number=tele,
            user=request.user,
        )

        CreateUserProfile.save()

        return redirect(reverse('home'))

def index_view(request):
    return render(request, 'base.html')

def about_us(request):
    return render(request, 'about_us.html')
def LoginView(request):
    return render(request, 'login.html')

def create_booking(request):
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save()
            return redirect('view_booking', booking_id=booking.id)
    else:
        booking_form = BookingForm()

    return render(request, 'create_booking.html', {'booking_form': booking_form})

