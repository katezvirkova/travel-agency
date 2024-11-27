from rest_framework import serializers
from .models import Destination
from users.serializers import UserSerializer

class DestinationSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)  # Serialize user data

    class Meta:
        model = Destination
        fields = ['id', 'name', 'slug', 'description', 'country', 'image_url', 'created_by', 'created_at', 'updated_at']
