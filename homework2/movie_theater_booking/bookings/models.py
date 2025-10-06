from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model) :
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    release_date = models.DateTimeField("release date")
    duration = models.DurationField()

class Seat(models.Model) :
    # Add choices for booking status
    # See https://docs.djangoproject.com/en/4.2/ref/models/fields/#choices
    PENDING = "PND"
    CONFIRMED = "CON"
    CANCELED = "CAN"
    COMPLETED = "COM"
    NO_SHOW = "NSH"
    UNSCHEDULED = "UNSCH"

    BOOKING_CHOICES = [ 
        (PENDING, "Pending"),
        (CONFIRMED, "Confirmed"),
        (CANCELED, "Canceled"),
        (COMPLETED, "Completed"),
        (NO_SHOW, "Now Show"),
        (UNSCHEDULED, "Unscheduled")
    ]

    seat_number = models.PositiveIntegerField("seat number")
    booking_status = models.CharField("booking status",max_length=5,choices=BOOKING_CHOICES,default=UNSCHEDULED)

class Booking(models.Model) :
    movie = models.CharField(max_length=200)
    seat = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    boooking_date = models.DateTimeField("booking date")
