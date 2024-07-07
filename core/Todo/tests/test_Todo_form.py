from django.test import TestCase
from Todo.forms import TaskForm


class TestTaskFrom(TestCase):

    def test_post_form_with_valid_data(self):
        form = TaskForm(data={
            "title":"pytest content",
            "content":"pytest content",
        })
        self.assertTrue(form.is_valid())