from rest_framework import serializers

from .models import Station, Travel

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = (
            'id',
            'name',
            'city',
            'state',
        )


class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = (
            'id',
            'departure_date',
            'arrival_date',
            'category',
            'origin',
            'destination',
            'departure_time',
            'arrival_time',
            'forecast',
            'price',
            'bus',
        )
        extra_kwargs = {
            'forecast': {'read_only': True},
        }