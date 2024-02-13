from django.contrib import admin

from .models import Bus

# Register your models here.
class BusAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'plate', 'available_seats', 'last_station', 'status')

admin.site.register(Bus, BusAdmin)