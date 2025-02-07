import os
import django
import pytz 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SabicAirlines.settings')  # Prilagodi ime ako je drugačije
django.setup()
import random
from datetime import datetime,timedelta
from AirlinesApp.models import Flight,Airport

airports_data = [
    {"name": "Heathrow Airport", "country": "UK", "city": "London"},
    {"name": "JFK International", "country": "USA", "city": "New York"},
    {"name": "Charles de Gaulle", "country": "France", "city": "Paris"},
    {"name": "Frankfurt Airport", "country": "Germany", "city": "Frankfurt"},
    {"name": "Dubai International", "country": "UAE", "city": "Dubai"},
    {"name": "Tokyo Haneda", "country": "Japan", "city": "Tokyo"},
    {"name": "Beijing Capital", "country": "China", "city": "Beijing"},
    {"name": "Los Angeles Intl", "country": "USA", "city": "Los Angeles"},
    {"name": "Sydney Airport", "country": "Australia", "city": "Sydney"},
    {"name": "Madrid-Barajas", "country": "Spain", "city": "Madrid"},
]

airports=[]
for airport in airports_data:
    obj,created=Airport.objects.get_or_create(**airport)
    airports.append(obj)

for _ in range(20):
    departure_airport,arrival_airport=random.sample(airports,2)
    departure_time=datetime.now(pytz.UTC)+timedelta(days=random.randint(1,30),hours=random.randint(1,12))
    arrival_time=departure_time+timedelta(hours=random.randint(1,12))

    flight=Flight.objects.create(
        flight_number=random.randint(1,1000),
        departure_airport=departure_airport,
        arrival_airport=arrival_airport,
        departure_time=departure_time,
        arrival_time=arrival_time,
        price=round(random.uniform(50,500),2),
        avaliable_seats=random.randint(50,200),
    )
    