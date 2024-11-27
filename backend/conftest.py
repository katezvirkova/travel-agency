import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import CustomUser
from destinations.models import Destination

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def travel_agent(db):
    return CustomUser.objects.create_user(
        username="travel_agent", email="travel_agent@example.com", password="password", is_travel_agent=True
    )

@pytest.fixture
def regular_user(db):
    return CustomUser.objects.create_user(
        username="regular_user", email="regular_user@example.com", password="password", is_travel_agent=False
    )


@pytest.fixture
def destination(db, travel_agent):
    return Destination.objects.create(
        name="Eiffel Tower",
        slug="eiffel-tower",
        description="A famous landmark in Paris.",
        country="France",
        created_by=travel_agent
    )


@pytest.fixture
def create_user(db):
    def make_user(username, email, password, is_travel_agent=False):
        return CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_travel_agent=is_travel_agent
        )
    return make_user

