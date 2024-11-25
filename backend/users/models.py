from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_travel_agent = models.BooleanField(default=False)  # Flag for agents who can manage destinations

    def __str__(self):
        return self.username
