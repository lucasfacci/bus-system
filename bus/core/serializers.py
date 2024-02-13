from rest_framework import serializers

from .models import Bus

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = (
            'id',
            'category',
            'plate',
            'available_seats',
            'last_station',
            'status',
        )