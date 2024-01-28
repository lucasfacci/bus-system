from rest_framework import serializers

from .models import Travel

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = (
            'id',
            'date',
            'category',
            'origin',
            'destination',
            'departure',
            'arrival',
            'forecast',
            'price',
        )
        extra_kwargs = {
            'forecast': {'read_only': True},
        }