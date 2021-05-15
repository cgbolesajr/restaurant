from django import forms
from .models import Reservation



class ReservationForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(
        attrs={'type': 'date'}
        ))
    time = forms.TimeField(widget=forms.TextInput(
        attrs={'type': 'time',}
        ))

    name = forms.CharField(widget=forms.TextInput(attrs={"class":'icon ion-android-person'}))

    class Meta:
        model = Reservation

        fields = "__all__"
