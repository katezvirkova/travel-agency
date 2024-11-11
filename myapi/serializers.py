from rest_framework import serializers
from .models import Hotel, Tour, Ticket

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'description', 'country', 'price', 'image']

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['id', 'name', 'description', 'country', 'image']

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'travel_type', 'departure_time', 'arrival_time', 'price', 'origin_city', 'destination_city']
