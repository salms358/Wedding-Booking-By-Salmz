# views.py
from django.shortcuts import render, redirect
from .models import Booking, Menu
from .forms import BookingForm, MenuForm

def create_booking(request):
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save()
            return redirect('view_booking', booking_id=booking.id)
    else:
        booking_form = BookingForm()
    return render(request, 'create_booking.html', {'booking_form': booking_form})

def view_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    menu = Menu.objects.get(booking=booking)
    return render(request, 'view_booking.html', {'booking': booking, 'menu': menu})

def update_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    menu = Menu.objects.get(booking=booking)

    if request.method == 'POST':
        booking_form = BookingForm(request.POST, instance=booking)
        menu_form = MenuForm(request.POST, instance=menu)
        if booking_form.is_valid() and menu_form.is_valid():
            booking_form.save()
            menu_form.save()
            return redirect('view_booking', booking_id=booking.id)
    else:
        booking_form = BookingForm(instance=booking)
        menu_form = MenuForm(instance=menu)

    return render(request, 'update_booking.html', {'booking_form': booking_form, 'menu_form': menu_form})

def cancel_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        booking.is_canceled = True
        booking.save()
        return redirect('view_booking', booking_id=booking.id)
    return render(request, 'cancel_booking.html', {'booking': booking})

