from rest_framework.viewsets import ModelViewSet
from .models import User,Flight,FlightClass,Ticket,Payment,Airport,Reservation,Cart
from .serializers import UserSerializer,FlightSerializer,FlightClassSerializer,TicketSerializer,PaymentSerializer,AirportSerializer,ReservationSerializer,CartSerializer
from .permissions import IsAdmin,IsCustomer,IsWorker,IsOwnerOrRead
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response


class AirportListCreateView(generics.ListCreateAPIView):
    queryset=Airport.objects.all()
    serializer_class=AirportSerializer

    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsAdmin()]
        return [IsAuthenticated()]
    
class AirportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Airport.objects.all()
    serializer_class=AirportSerializer
    def get_permissions(self):
        if self.request.method in ['PUT','PATCH','DELETE']:
            return [IsAdmin()]
        return [IsAuthenticated()]
    
class FlightListCreateView(generics.ListCreateAPIView):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer
    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsAdmin()]
        return [IsAuthenticated()]
    
class FlightRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer
    def get_permissions(self):
        if self.request.method in ['PUT','PATCH','DELETE']:
            return [IsAdmin()]
        return [IsAuthenticated()]
    
class FlightClassListCreateView(generics.ListCreateAPIView):
    queryset=FlightClass.objects.all()
    serializer_class=FlightClassSerializer
    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsAdmin()]
        return [IsAuthenticated()]
    
class FlightClassRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset=FlightClass.objects.all()
    serializer_class=FlightClassSerializer
    def get_permissions(self):
        if self.request.method in ['PUT','PATCH','DELETE']:
            return [IsAdmin()]
        return [IsAuthenticated()]
    
class UserListCreateView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsAdmin()]
        return [IsAuthenticated()]
    
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    def get_permissions(self):
        if self.request.method in ['PUT','PATCH','DELETE']:
            return [IsAdmin()]
        return [IsAuthenticated()]
    
    
class ReservationListCreateView(generics.ListCreateAPIView):
    queryset=Reservation.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=ReservationSerializer
    def get_queryset(self):
        if self.request.user.is_staff:
            return Reservation.objects.all()
        return Reservation.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReservationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    def get_queryset(self):
        if self.request.user.is_staff:
            return Reservation.objects.all()
        return Reservation.objects.filter(user=self.request.user)
    def get_permissions(self):
        if self.request.method in ['PUT','PATCH','DELETE']:
            return [IsAdmin()]
        return [IsAuthenticated()]
    def get_object(self):
        obj = super().get_object()
        if not self.request.user.is_staff and obj.user != self.request.user:
            raise PermissionDenied("You do not have a permission for this reservation!")
        return obj

class CheckoutView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        cart=Cart.objects.filter(user=request.user)
        if not cart:
            return Response({"Error":"Cart is empty"},status=status.HTTP_400_BAD_REQUEST)
        for reservation in cart.reservations.all():
            if reservation.flight.avaliable_seats<1:
                return Response({"Error":"The flight is full!"},status=status.HTTP_400_BAD_REQUEST)
            
        payment=Payment.objects.create(user=request.user,amount=cart.get_total_price(),status="Completed")

        for reservation in cart.reservations.all():
            Ticket.objects.create(user=request.user,reservation=reservation,payment=payment)

        cart.delete()
        return Response({"success": "Payment completed, tickets issued!"}, status=status.HTTP_201_CREATED)

