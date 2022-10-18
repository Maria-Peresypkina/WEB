from django.contrib import admin
from .models import Accommodation
from .models import Guest
from .models import Booking

# Register your models here.
admin.site.register(Accommodation)
admin.site.register(Guest)
admin.site.register(Booking)