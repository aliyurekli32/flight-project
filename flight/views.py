from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FlightSerializer
from .models import Flight


# Create your views here.
class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer