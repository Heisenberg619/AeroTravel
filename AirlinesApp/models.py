from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES=[
        ('admin','Admin'),
        ('worker','Worker'),
        ('customer','Customer'),
    ]

    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=20,blank=True,null=True)
    role=models.CharField(max_length=20,choices=ROLE_CHOICES,default='customer')
    
class Airport(models.Model):
    name=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

class FlightClass(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()

class Flight(models.Model):
    flight_number=models.CharField(max_length=10)
    departure_airport=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='departure_flights')
    arrival_airport=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='arrival_flights')
    departure_time=models.DateTimeField()
    arrival_time=models.DateTimeField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    flight_class=models.ForeignKey(FlightClass,on_delete=models.CASCADE)
    avaliable_seats=models.IntegerField()

class Reservation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
    number_of_tickets=models.IntegerField()
    status=models.CharField(max_length=20,choices=[('booked','Booked'),('cancelled','Cancelled')])
    created_at=models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    reservation=models.ForeignKey(Reservation,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    payment_method=models.CharField(max_length=50)
    payment_status=models.CharField(max_length=10,choices=[('paid','Paid'),('failed','Failed')])
    payment_date=models.DateTimeField()

class Ticket(models.Model):
    reservation=models.ForeignKey(Reservation,on_delete=models.CASCADE)
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
    ticket_number=models.CharField(max_length=20,unique=True)
    seat_number=models.CharField(max_length=10)

