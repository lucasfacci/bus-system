from django.core.serializers import serialize
from rest_framework import viewsets

from .models import Travel
from .serializers import TravelSerializer

# Create your views here.
class TravelViewSet(viewsets.ModelViewSet):
    """
    Travels
    """
    serializer_class = TravelSerializer
    queryset = Travel.objects.all()