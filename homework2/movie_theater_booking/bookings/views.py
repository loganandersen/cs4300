from django.shortcuts import render
from rest_framework import viewsets
from bookings.serializers import MovieSerializer, SeatSerializer, BookingSerializer

# Create your views here.
class MovieViewset(viewsets.ModelViewSet) :
    queryset = Movie.objects.all().order_by("")