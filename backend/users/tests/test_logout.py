from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

class LogoutViewTest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            username="testuser", password="password123"
        )
        self.client.force_authenticate(user=self.user)

    def test_logout_success(self):
        # Generate a refresh token for the authenticated user
        refresh = RefreshToken.for_user(self.user)
        refresh_token = str(refresh)
        print(f"Generated refresh token: {refresh_token}")  # Print to debug

        # Make a POST request to the logout endpoint with correct Content-Type
        response = self.client.post(
            "/users/logout/",
            {"refresh": refresh_token},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_logout_missing_refresh_token(self):
        # Make a POST request without a refresh token
        response = self.client.post("/users/logout/", format='json')

        # Assert the response status is 400 Bad Request and the detail message
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["detail"], "Refresh token missing")

    def test_logout_invalid_refresh_token(self):
        # Use an invalid refresh token
        response = self.client.post("/users/logout/", {"refresh": "invalid_token"}, format='json')

        # Assert the response status is 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("detail", response.data)

