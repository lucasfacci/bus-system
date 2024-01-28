from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
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