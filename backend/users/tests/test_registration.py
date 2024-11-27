import pytest
from rest_framework import status
from users.models import CustomUser

@pytest.mark.django_db
def test_register_user(api_client):
    data = {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "newpassword",
    }
    response = api_client.post("/users/register/", data)
    assert response.status_code == status.HTTP_201_CREATED
    assert "access" in response.data
    assert "refresh" in response.data
    assert CustomUser.objects.filter(username="newuser").exists()

@pytest.mark.django_db
def test_register_user_with_duplicate_email(api_client, create_user):
    create_user("existinguser", "existing@example.com", "password")
    data = {
        "username": "newuser",
        "email": "existing@example.com",  # Duplicate email
        "password": "newpassword",
    }
    response = api_client.post("/users/register/", data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "email" in response.data
