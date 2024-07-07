from django.test import TestCase
from Todo.models import Task
from accounts.models import User , Profile

class TestTaskModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="example@example.com",password="a/1234567")
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="test first_name",
            last_name="test last_name",
            description="test description"
            )
    
    def test_create_post_with_valid_data(self):
        task = Task.objects.create(
            author = self.profile,
            title = "test",
            content = "description",
            status = False,
            ) 
        self.assertTrue(Task.objects.filter(pk=task.pk).exists())
