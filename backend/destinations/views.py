from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Destination
from .serializers import DestinationSerializer

class DestinationList(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        destinations = Destination.objects.all()
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_travel_agent:  # Only travel agents can add destinations
            return Response({"error": "Only travel agents can add destinations."}, status=status.HTTP_403_FORBIDDEN)

        serializer = DestinationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)  # Automatically set the creator
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DestinationDetail(APIView):
    # permission_classes = [IsAuthenticated]

    def get_object(self, slug):
        try:
            return Destination.objects.get(slug=slug)
        except Destination.DoesNotExist:
            return None

    def get(self, request, slug):
        destination = self.get_object(slug)
        if not destination:
            return Response({"error": "Destination not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DestinationSerializer(destination)
        return Response(serializer.data)

    def put(self, request, slug):
        destination = self.get_object(slug)
        if not destination:
            return Response({"error": "Destination not found."}, status=status.HTTP_404_NOT_FOUND)

        if destination.created_by != request.user:
            return Response({"error": "You can only update your own destinations."}, status=status.HTTP_403_FORBIDDEN)

        serializer = DestinationSerializer(destination, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        destination = self.get_object(slug)
        if not destination:
            return Response({"error": "Destination not found."}, status=status.HTTP_404_NOT_FOUND)

        if destination.created_by != request.user:
            return Response({"error": "You can only delete your own destinations."}, status=status.HTTP_403_FORBIDDEN)

        destination.delete()
        return Response({"message": "Destination deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
