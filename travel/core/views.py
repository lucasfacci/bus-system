from django.core.serializers import serialize
from rest_framework import viewsets

from .models import Station, Travel
from .serializers import StationSerializer, TravelSerializer

# Create your views here.
class StationViewSet(viewsets.ModelViewSet):
    """
    Stations
    """
    serializer_class = StationSerializer
    queryset = Station.objects.all()


class TravelViewSet(viewsets.ModelViewSet):
    """
    Travels
    """
    serializer_class = TravelSerializer
    queryset = Travel.objects.all()