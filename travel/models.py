from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Route_shedule(models.Model):
    
    serial_number = models.AutoField(primary_key=True)
    route_number = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=100)
    airline_name = models.CharField(max_length=100)
    flight = models.CharField(max_length=100)
    departure_airport = models.CharField(max_length=100)
    arrival_airport = models.CharField(max_length=100)
    departure_date = models.DateField(auto_now_add=False)
    departure_time = models.TimeField(auto_now_add=False)
    flight_delay = models.TimeField(auto_now_add=False,null=True)
    arrival_date = models.DateField(auto_now_add=False)
    arrival_time = models.TimeField(auto_now_add=False) 
    flight_status = models.CharField(max_length=100,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return str(self.flight_number + " " + self.departure_airport + " to " + self.arrival_airport)
    

class Bookings(models.Model):
    name = models.CharField(max_length=20)
    number_of_passengers = models.IntegerField()
    passport_number = models.CharField(max_length=20)
    house = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=255)
    phone= models.IntegerField()
    filght = models.ForeignKey(Route_shedule,on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
    
    
    