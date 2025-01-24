from rest_framework.viewsets import ModelViewSet
from .models import User,Flight,FlightClass,Ticket,Payment,Airport,Reservation
from .serializers import UserSerializer,FlightSerializer,FlightClassSerializer,TicketSerializer,PaymentSerializer,AirportSerializer,ReservationSerializer
from .permissions import IsAdmin,IsCustomer,IsWorker,IsOwnerOrRead

class FlightViewSet(ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAdmin()]
        return super().get_permissions()
    
class FlightClassViewSet(ModelViewSet):
    queryset=FlightClass.objects.all()
    serializer_class=FlightClassSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [IsAdmin()]
        return super().get_permissions()
    
class AirportClassViewSet(ModelViewSet):
    queryset=Airport.objects.all()
    serializer_class=AirportSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [IsAdmin()]
        return super().get_permissions()
    
class ReservationViewSet(ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer

    def get_permissions(self):
        if self.action in ['retrieve','update','partial_update','destroy']:
            return [IsOwnerOrRead()]
        elif self.action == 'list':
            return [IsAdmin()]
        return super().get_permissions()
    
class PaymentViewSet(ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer

    def get_queryset(self):
        if self.request.user.is_staff():
            return Payment.objects.all()
        return Payment.objects.filter(user=self.request.user)
    
    def get_permissions(self):
        if self.action in ['list','retrieve']:
            return [IsOwnerOrRead()]
        elif self.action in ['update','partial_update','destroy']:
            return [IsAdmin()]
        return super().get_permissions()

class TicketViewSet(ModelViewSet):
    queryset=Ticket.objects.all()
    serializer_class=TicketSerializer

    def get_queryset(self):
        if self.request.user.is_staff():
            return Ticket.objects.all()
        return Ticket.objects.filter(user=self.request.user)
    
    def get_permissions(self):
        if self.action in ['list','retrieve']:
            return [IsOwnerOrRead()]
        elif self.action in ['update','partial_update','destroy']:
            return [IsAdmin()]
        return super().get_permissions()

class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

    def get_permissions(self):
        return super().get_permissions()
    