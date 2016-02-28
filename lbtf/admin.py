from django.contrib import admin

from .models import Brewery, Beer, Event, Event_Brewery, Event_Beer

admin.site.register(Brewery)
admin.site.register(Beer)
admin.site.register(Event)
admin.site.register(Event_Brewery)
admin.site.register(Event_Beer)
