from django.shortcuts import render

# Create your views here.
from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import *
from .models import *
from .forms import *
from django.contrib.auth.mixins import *
# Create your views here.   

class TaskListView(LoginRequiredMixin,ListView):
    queryset = Task.objects.all()
    context_object_name = 'Tasks'
    ordering = '-created_date'
    def get_queryset(self):
        profile =  Profile.objects.get(user=self.request.user)
        return Task.objects.filter(author=profile)

class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    
    
class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm
    success_url = '/task/'
    
    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.author = profile
        return super().form_valid(form)

class TaskEditView(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = TaskForm
    success_url = '/task/'

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    success_url = '/task/'

def change_to_done(self,pk):
    task = Task.objects.get(pk=pk)
    task.status = True
    task.save()
    return redirect('/task/')
def change_to_not_done(self,pk):
    task = Task.objects.get(pk=pk)
    task.status = False
    task.save()
    return redirect('/task/')
