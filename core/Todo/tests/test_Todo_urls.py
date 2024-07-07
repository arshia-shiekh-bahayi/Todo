from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from ..views import TaskListView , TaskDetailView

class TestTodoUrl(SimpleTestCase):

    def test_Todo_task_list_url_resolve(self):
        url = reverse("task:Task-list")
        self.assertEqual(resolve(url).func.view_class, TaskListView)

    def test_Todo_detail_list_url_resolve(self):
        url = reverse("task:Task-detail",kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class, TaskDetailView)