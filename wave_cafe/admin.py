from django.contrib import admin
from .models import Reservation_Data
from .models import Franchise_Data
from .models import Contact_Data

# Register your models here.

admin.site.register(Reservation_Data)
admin.site.register(Franchise_Data)
admin.site.register(Contact_Data)