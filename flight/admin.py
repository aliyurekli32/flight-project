from django.contrib import admin

# Register your models here.

from .models import Flight, Passenger, Reservation

# Register your models here.
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Reservation)
