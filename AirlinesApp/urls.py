from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FlightViewSet, FlightClassViewSet, ReservationViewSet, PaymentViewSet, TicketViewSet, AirportViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'reservations', ReservationViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'users', UserViewSet)
router.register(r'airports', AirportViewSet)
router.register(r'flights', FlightViewSet)
router.register(r'flight_classes', FlightClassViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # Token JWT authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
