from django.urls import path
from .views import DestinationList, DestinationDetail

urlpatterns = [
    path('', DestinationList.as_view(), name='destination_list'),
    path('<slug:slug>/', DestinationDetail.as_view(), name='destination_detail'),
]
