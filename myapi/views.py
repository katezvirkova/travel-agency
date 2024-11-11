from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Hotel, Tour, Ticket
from .serializers import HotelSerializer, TourSerializer, TicketSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Отримання токену
class TokenObtainPairView(APIView):
    def post(self, request):
        refresh = RefreshToken.for_user(request.user)
        access_token = refresh.access_token
        return Response({'access': str(access_token), 'refresh': str(refresh)})

# Відображення готелів
class HotelListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

# Відображення турів
class TourListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data)

# Відображення квитків
class TicketListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        tickets = Ticket.objects.filter(user=request.user)
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

# Додавання в улюблені (просто приклад)
class FavoriteHotelView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        hotel_id = request.data.get('hotel_id')
        hotel = Hotel.objects.get(id=hotel_id)
        request.user.favorite_hotels.add(hotel)
        return Response({"message": "Hotel added to favorites"})

# Create your views here.
