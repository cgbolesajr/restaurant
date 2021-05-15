from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm


# Create your views here.
def reservation(request):
    reserve_form = ReservationForm()

    if request.method == 'POST':
        reserve_form = ReservationForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
            return redirect('reservation')
    context = {
        "form": reserve_form
    }
    return render(request,'reservation/reservation.html',context)
