from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User , Profile
from Todo.models import Task

class TestTodoView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email="example@example.com",password="a/1234567")
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="test first_name",
            last_name="test last_name",
            description="test description"
        )
        self.task = Task.objects.create(
            author = self.profile,
            title = "pytest title",
            content = "pytest content",
            status = False
        )


    def test_Todo_task_detail_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse('task:Task-detail',kwargs={'pk':self.task.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_Todo_task_detail_anonymous_response(self):
        url = reverse('task:Task-detail',kwargs={'pk':self.task.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)