from django.contrib import admin

from speakers.models import Speaker
from flight_options.models import FlightOption


class FlightOptionsInline(admin.StackedInline):
    model = FlightOption
    extra=0

class SpeakerAdmin(admin.ModelAdmin):
    list_filter = 'waiting_flight', 'flight_arranged'
    inlines = [FlightOptionsInline]


admin.site.register(Speaker, SpeakerAdmin)