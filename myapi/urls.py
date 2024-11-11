from django.urls import path
from .views import HotelListView, TourListView, TicketListView, TokenObtainPairView

urlpatterns = [
    path('api/hotels/', HotelListView.as_view(), name='hotel-list'),
    path('api/tours/', TourListView.as_view(), name='tour-list'),
    path('api/tickets/', TicketListView.as_view(), name='ticket-list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
