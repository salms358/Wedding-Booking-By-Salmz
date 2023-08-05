from django.shortcuts import render
from .forms import BookingForm 

def index_view(request):
    return render(request, 'base.html')
def about_us(request):
    return render(request, 'about_us.html')
def register(request):
    return render(request, 'register.html')


def create_booking(request):
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save()
            return redirect('view_booking', booking_id=booking.id)
    else:
        booking_form = BookingForm()
    return render(request, 'create_booking.html', {'booking_form': booking_form})

