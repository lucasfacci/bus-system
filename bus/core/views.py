from rest_framework import viewsets

from .models import Bus
from .serializers import BusSerializer

# Create your views here.
class BusViewSet(viewsets.ModelViewSet):
    """
    Buses
    """
    serializer_class = BusSerializer
    queryset = Bus.objects.all()