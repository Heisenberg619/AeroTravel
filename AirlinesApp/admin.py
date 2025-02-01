from django.contrib import admin
from .models import User  # Tvoj custom User model

# Koristi Django-ov UserAdmin za prikazivanje u admin panelu
admin.site.register(User)