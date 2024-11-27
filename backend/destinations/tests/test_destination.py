import pytest
from rest_framework import status
from destinations.models import Destination

@pytest.mark.django_db
def test_get_destinations(api_client, destination):
    response = api_client.get("/destinations/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["name"] == destination.name

@pytest.mark.django_db
def test_post_destination_as_travel_agent(api_client, travel_agent):
    api_client.force_authenticate(user=travel_agent)
    data = {
        "name": "Great Wall of China",
        "slug": "great-wall-of-china",
        "description": "A historic wall in China.",
        "country": "China",
        "image_url": "https://example.com/great_wall.jpg"
    }
    response = api_client.post("/destinations/", data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Destination.objects.filter(name="Great Wall of China").exists()

@pytest.mark.django_db
def test_post_destination_as_regular_user(api_client, regular_user):
    api_client.force_authenticate(user=regular_user)
    data = {
        "name": "Great Wall of China",
        "slug": "great-wall-of-china",
        "description": "A historic wall in China.",
        "country": "China",
        "image_url": "https://example.com/great_wall.jpg"
    }
    response = api_client.post("/destinations/", data)
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_get_single_destination(api_client, destination):
    response = api_client.get(f"/destinations/{destination.slug}/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == destination.name

@pytest.mark.django_db
def test_update_destination(api_client, destination, travel_agent):
    api_client.force_authenticate(user=travel_agent)
    data = {"name": "Eiffel Tower Updated"}
    response = api_client.put(f"/destinations/{destination.slug}/", data)
    assert response.status_code == status.HTTP_200_OK
    destination.refresh_from_db()
    assert destination.name == "Eiffel Tower Updated"

@pytest.mark.django_db
def test_update_destination_by_non_creator(api_client, destination, regular_user):
    api_client.force_authenticate(user=regular_user)
    data = {"name": "Eiffel Tower Updated"}
    response = api_client.put(f"/destinations/{destination.slug}/", data)
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_update_destination(api_client, destination, travel_agent):
    api_client.force_authenticate(user=travel_agent)
    data = {
        "name": "Eiffel Tower Updated",
        "slug": destination.slug,  # Reuse the existing slug
        "description": destination.description,
        "country": destination.country,
    }
    response = api_client.put(f"/destinations/{destination.slug}/", data)
    assert response.status_code == status.HTTP_200_OK
    destination.refresh_from_db()
    assert destination.name == "Eiffel Tower Updated"


@pytest.mark.django_db
def test_delete_destination_by_non_creator(api_client, destination, regular_user):
    api_client.force_authenticate(user=regular_user)
    response = api_client.delete(f"/destinations/{destination.slug}/")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert Destination.objects.filter(slug=destination.slug).exists()
