from rest_framework.test import APIClient
from django.urls import reverse
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
        response = api_client.get(url,user=user)
        assert response.status_code == 200