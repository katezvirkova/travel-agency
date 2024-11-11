from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='hotels/')

    def __str__(self):
        return self.name


class Tour(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tours/')

    def __str__(self):
        return self.name


class Ticket(models.Model):
    travel_type_choices = [
        ('flight', 'Літак'),
        ('train', 'Потяг'),
        ('bus', 'Автобус')
    ]
    travel_type = models.CharField(choices=travel_type_choices, max_length=10)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    origin_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')

    def __str__(self):
        return f'{self.travel_type} {self.origin_city} -> {self.destination_city}'


