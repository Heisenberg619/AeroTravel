from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,FlightViewSet,FlightClassViewSet,ReservationViewSet,PaymentViewSet,TicketViewSet,AirportViewSet
from rest_framework.authtoken.views import obtain_auth_token

router=DefaultRouter()
router.register(r'reservations',ReservationViewSet)
router.register(r'payments',PaymentViewSet)
router.register(r'tickets',TicketViewSet)
router.register(r'users',UserViewSet)
router.register(r'airports',AirportViewSet)
router.register(r'flights',FlightViewSet)
router.register(r'flight_classes',FlightClassViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('api/auth/token/',obtain_auth_token),
]