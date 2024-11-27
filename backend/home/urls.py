from django.urls import path
from .views import homepage, about_page, contact_page

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
]
