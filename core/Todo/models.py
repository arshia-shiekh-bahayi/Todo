from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import *
# User = get_user_model()
# Create your models here.
class Task(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_snippet(self):
       return self.content[0:5]
    def get_absolute_api_url(self):
       return reverse("task:api-v1:task-detail", kwargs={"pk":self.pk})