from django.contrib import admin

from .models import Travel

# Register your models here.
class TravelAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'category', 'origin', 'destination', 'departure', 'arrival', 'forecast', 'price', 'created', 'updated')
    readonly_fields = ('forecast',)


admin.site.register(Travel, TravelAdmin)