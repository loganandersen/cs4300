from django.shortcuts import render
from rest_framework import viewsets
from bookings.serializers import MovieSerializer, SeatSerializer, BookingSerializer
from bookings.models import Movie, Seat, Booking

# Create your views here.
class MovieViewset(viewsets.ModelViewSet) :
    queryset = Movie.objects.all().order_by("title")
    serializer_class = MovieSerializer

class SeatViewset(viewsets.ModelViewSet) :
    queryset = Seat.objects.all().order_by("seat_number")
    serializer_class = SeatSerializer

class BookingViewset(viewsets.ModelViewSet) :
    queryset = Booking.objects.all().order_by("boooking_date")
    serializer_class = BookingSerializer
