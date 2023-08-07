from django.shortcuts import render
from .forms import BookingForm
from django.views import generic, View
from django.views.generic import TemplateView, DeleteView 

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
class CreateProfile(View):
    template_name = "create_profile.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "register.html",
        )
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
