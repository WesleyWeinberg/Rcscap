from django.contrib import admin

from .models import PromoName, Meeting, Event

admin.site.register(PromoName)
admin.site.register(Meeting)
admin.site.register(Event)
