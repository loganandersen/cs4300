from django.shortcuts import render
from rest_framework import viewsets
from bookings.serializers import MovieSerializer, SeatSerializer, BookingSerializer

# Create your views here.
class MovieViewset(viewsets.ModelViewSet) :
    queryset = Movie.objects.all().order_by("title")
    serializers_class = MovieSerializer

class SeatViewset(viewsets.ModelViewSet) :
    queryset = Seat.objects.all().order_by("seat_number")
    serializers_class = SeatSerializer

class BookingViewset(viewsets.ModelViewSet) :
    queryset = Booking.objects.all().order_by("boooking_date")
    serializers_class = BookingSerializer
