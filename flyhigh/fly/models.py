from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Flights(models.Model):
    flight_name=models.CharField(max_length=50, primary_key=True)
    flight_logo=models.ImageField(upload_to='fly/images')
    def __str__(self):
        return str(self.flight_name)

class Roots(models.Model):
    flight_name=models.ForeignKey(Flights,on_delete=models.CASCADE)
    dep_airport=models.CharField(max_length=50)
    dep_time=models.TimeField(auto_now=False, auto_now_add=False)
    arr_airport=models.CharField(max_length=50)
    arr_time=models.TimeField(auto_now=False, auto_now_add=False)
    # travel_time=models.TimeField(auto_now=False, auto_now_add=False)
    travel_time=models.DurationField(null=True,blank=True)
    cls=models.CharField(max_length=50,choices=[('Economy Class','Economy Class'),('Business Class','Business Class'),('First Class','First Class')])
    total_fare=models.IntegerField()     

    def __str__(self):
        s = f'{str(self.flight_name)} - {self.dep_airport} To {self.arr_airport}'
        return str(s)

    @property
    def rootd(self):
        s = f'{str(self.flight_name)} - {self.dep_airport} To {self.arr_airport}'
        return s
    
class ConfirmBooking(models.Model):
    bookUser = models.ForeignKey(User, on_delete=models.CASCADE)
    journey_details=models.ForeignKey(Roots,on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=50)
    address=models.TextField()
    vaccine=models.CharField(max_length=50)
    gender=models.CharField(max_length=50,choices=[('M','Male'),('F','Female')])
    totalfare=models.IntegerField()
    passenger = models.IntegerField()
    journey_date = models.DateField(auto_now=True, auto_now_add=False) 