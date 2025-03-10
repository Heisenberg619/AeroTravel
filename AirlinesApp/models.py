from django.db import models
from django.contrib.auth.models import User

class Airport(models.Model):
    name=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class FlightClass(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    def __str__(self):
        return f"{self.name}"

class Flight(models.Model):
    flight_number=models.CharField(max_length=10)
    departure_airport=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='departure_flights')
    arrival_airport=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='arrival_flights')
    departure_time=models.DateTimeField()
    arrival_time=models.DateTimeField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    avaliable_seats=models.IntegerField()

    def __str__(self):
        return f"{self.flight_number}"

class Reservation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
    number_of_tickets=models.IntegerField()
    status=models.CharField(max_length=20,choices=[('booked','Booked'),('cancelled','Cancelled')])
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"

class Payment(models.Model):
    reservation=models.ForeignKey(Reservation,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    payment_method=models.CharField(max_length=50)
    payment_status=models.CharField(max_length=10,choices=[('paid','Paid'),('failed','Failed')])
    payment_date=models.DateTimeField()

    def __str__(self):
        return f"{self.id}"

class Ticket(models.Model):
    reservation=models.ForeignKey(Reservation,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True)
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
    ticket_number=models.CharField(max_length=20,unique=True)
    seat_number=models.CharField(max_length=10)
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    reservations=models.ManyToManyField(Reservation)
