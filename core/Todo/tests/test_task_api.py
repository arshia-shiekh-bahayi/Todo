from rest_framework.test import APIClient
from django.urls import reverse , resolve
import pytest
from datetime import datetime
from accounts.models import User

@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def common_user():
    user = User.objects.create_user(email="example@example.com", password="a/@1234567",is_verified=True)
    return user

@pytest.mark.django_db
class TestTaskApi:

    def test_get_task_response_200_status(self,api_client,common_user):
        url = reverse("task:api-v1:task-list")
        user = common_user
        api_client.force_login(user=user)
        response = api_client.get(url)
        assert response.status_code == 200
    
    
    def test_create_task_response_404_status(self,api_client):
        url = reverse("task:api-v1:task-list")
        response = api_client.get(url)
        print(response)
        assert response.status_code == 404

    def test_create_task_response_201_status(self,api_client,common_user):
        url = reverse("task:api-v1:task-list")
        data = {
            "title":"pytest",
            "content":"pytest content",
        }
        user = common_user
        api_client.force_login(user=user)
        response = api_client.post(url,data)
        assert response.status_code == 201

    def test_create_post_invalid_data_response_400_status(self,api_client,common_user):
        url = reverse("task:api-v1:task-list")
        data = {
            "title":"pytest"
        }
        user = common_user
        api_client.force_login(user=user)
        response = api_client.post(url,data)
        assert response.status_code == 400

    

    