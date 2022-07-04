from django.contrib import admin
from .models import Flights,Roots,ConfirmBooking

# Register your models here.
@admin.register(Flights)
class FlightsAdmin(admin.ModelAdmin):
    list_display = ['flight_name','flight_logo']
@admin.register(Roots)
class RootsAdmin(admin.ModelAdmin):
    list_display = ['flight_name','id','dep_airport','arr_airport','cls','total_fare']
@admin.register(ConfirmBooking)
class ConfirmBookingAdmin(admin.ModelAdmin):
    list_display = ['journey_details']