from rest_framework import serializers
from .models import User,Flight,Reservation,Ticket,Payment,Airport,FlightClass,Cart


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields=['flight_number','departure_airport','arrival_airport','departure_time','arrival_time','price','avaliable_seats']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields=['flight','number_of_tickets','status']

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ticket
        fields=['reservation','payment','flight','ticket_number','seat_number','issued_at']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields=['reservation','amount','payment_method','payment_status']

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Airport
        fields=['name','country','city']

class FlightClassSerializer(serializers.ModelSerializer):
    class Meta:
        model=FlightClass
        fields=['name','description']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=['user','reservations']