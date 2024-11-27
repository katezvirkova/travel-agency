from django.urls import path
from .views import DestinationList, DestinationDetail

urlpatterns = [
    path('', DestinationList.as_view(), name='destination_list'),
    path("<str:name>/", DestinationDetail.as_view(), name="destination-detail"),

]
