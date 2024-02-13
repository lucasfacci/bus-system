from django.contrib import admin

from .models import Station, Travel

# Register your models here.
class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'state')

class TravelAdmin(admin.ModelAdmin):
    list_display = ('id', 'departure_date', 'arrival_date', 'category', 'origin', 'destination', 'departure_time', 'arrival_time', 'price', 'created', 'updated')
    readonly_fields = ('forecast',)

admin.site.register(Station, StationAdmin)
admin.site.register(Travel, TravelAdmin)