# Make serializers for the models
from bookings.models import Movie, Seat, Booking
from rest_framework import serializers

class MovieSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = Movie
        fields = ['title', 'description', 'release_date', 'duration']

class SeatSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = Seat
        fields = ['seat_number', 'booking_status']

class BookingSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Booking
        fields = ['movie', 'seat', 'user', 'boooking_date'] 
