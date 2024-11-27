import pytest
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# LoginView Tests
@pytest.mark.django_db
def test_login_user(api_client, create_user):
    create_user("testuser", "testuser@example.com", "testpassword")
    data = {
        "username": "testuser",
        "password": "testpassword",
    }
    response = api_client.post("/users/login/", data)
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert "refresh" in response.data



@pytest.mark.django_db
def test_login_with_invalid_credentials(api_client, create_user):
    create_user("testuser", "testuser@example.com", "testpassword")
    data = {
        "username": "testuser",
        "password": "wrongpassword",
    }
    response = api_client.post("/users/login/", data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

# TokenRefreshView Tests
@pytest.mark.django_db
def test_refresh_access_token(api_client, create_user):
    user = create_user("testuser", "testuser@example.com", "testpassword")
    refresh = RefreshToken.for_user(user)
    data = {"refresh": str(refresh)}
    response = api_client.post("/users/token/refresh/", data)
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data

@pytest.mark.django_db
def test_refresh_access_token_invalid(api_client):
    data = {"refresh": "invalid_token"}
    response = api_client.post("/users/token/refresh/", data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

