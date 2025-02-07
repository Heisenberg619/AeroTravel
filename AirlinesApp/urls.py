from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    AirportListCreateView, AirportRetrieveUpdateDestroyView,
    FlightListCreateView, FlightRetrieveUpdateDestroyView,
    FlightClassListCreateView, FlightClassRetrieveUpdateDestroyView,
    UserListCreateView, UserRetrieveUpdateDestroyView,
    ReservationListCreateView, ReservationRetrieveUpdateDestroyView
)

urlpatterns = [
    # Token JWT authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/airports/',AirportListCreateView.as_view(),name='airport-list-create'),
    path('api/airports/<int:pk>',AirportRetrieveUpdateDestroyView.as_view(),name='airport-detail'),

    path('api/flights/',FlightListCreateView.as_view(),name='flight-list-create'),
    path('api/flights/<int:pk>',FlightRetrieveUpdateDestroyView.as_view(),name='flight-detail'),

    path('api/flight_classes/',FlightClassListCreateView.as_view(),name='flight-class-list-create'),
    path('api/flight_classes/<int:pk>',FlightClassRetrieveUpdateDestroyView.as_view(),name='flight-class-detail'),
    
    path('api/users/', UserListCreateView.as_view(), name='user-list-create'),
    path('api/users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),

    path('api/reservations/', ReservationListCreateView.as_view(), name='reservation-list-create'),
    path('api/reservations/<int:pk>/', ReservationRetrieveUpdateDestroyView.as_view(), name='reservation-detail'),


]
