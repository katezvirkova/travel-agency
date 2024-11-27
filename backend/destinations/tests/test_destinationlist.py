import pytest
from rest_framework import status
from destinations.models import Destination
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_view_destinations(api_client):
    # Create a destination
    destination = Destination.objects.create(
        name="Paris",
        slug="paris",
        country="France",
        description="The capital of France",
        image_url="https://example.com/paris.jpg"
    )

    # Requesting the destinations list
    response = api_client.get('/destinations/')

    # Check that the response is valid and contains the destination
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0
    assert response.data[0]['name'] == destination.name


@pytest.mark.django_db
def test_create_destination_as_travel_agent(api_client):
    # Create a travel agent user
    user = User.objects.create_user(username='travelagent', password='password')
    user.is_travel_agent = True  # Assuming is_travel_agent is a custom field
    user.save()

    # Login and get token for the user
    response = api_client.post('/api/token/', {'username': 'travelagent', 'password': 'password'})
    access_token = response.data['access']

    # Define destination data
    data = {
        'name': 'New York',
        'slug': 'new-york',
        'country': 'USA',
        'description': 'A beautiful city',
        'image_url': 'https://example.com/ny.jpg'
    }

    # Send a POST request to create a destination
    response = api_client.post(
        '/destinations/',
        data,
        HTTP_AUTHORIZATION=f'Bearer {access_token}'
    )

    # Assert that the destination was created
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'New York'


@pytest.mark.django_db
def test_create_destination_as_non_travel_agent(api_client):
    # Create a non-travel agent user
    user = User.objects.create_user(username='user', password='password')

    # Login and get token for the user
    response = api_client.post('/api/token/', {'username': 'user', 'password': 'password'})
    access_token = response.data['access']

    # Define destination data
    data = {
        'name': 'Tokyo',
        'slug': 'tokyo',
        'country': 'Japan',
        'description': 'The capital of Japan',
        'image_url': 'https://example.com/tokyo.jpg'
    }

    # Send a POST request to create a destination
    response = api_client.post(
        '/destinations/',
        data,
        HTTP_AUTHORIZATION=f'Bearer {access_token}'
    )

    # Assert that the user cannot create destinations
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data['error'] == 'Only travel agents can add destinations.'
