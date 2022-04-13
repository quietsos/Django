from django.contrib import admin

# Register your models here.
from . models import Venue
from . models import Users
from . models import Event

admin.site.register(Venue)
admin.site.register(Users)
admin.site.register(Event)



