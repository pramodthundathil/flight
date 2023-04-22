from django import forms
from .models import Route_shedule, Bookings
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

  
class Route_shedule_form(forms.ModelForm):
  
    class Meta:
        model = Route_shedule
        fields = ['route_number','flight_number','airline_name','flight','departure_airport','arrival_airport','departure_date','departure_time','arrival_date','arrival_time']



# from django import forms
# from django.forms import forms
# from .models import Route_shedule
# from django.forms import ModelForm

# class Route_shedule_form(forms.ModelForm):
    
#     class meta:
#         model = Route_shedule
#         fields = ['route_number','flight_number','airline_name','flight','departure_airport','arrival_airport','departure_time','arrival_time']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ["name","number_of_passengers","passport_number","house","city","state","country","phone"]