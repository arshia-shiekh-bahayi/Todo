from django.urls import path
from django.views.generic import *
from .views import *
app_name = 'task'
urlpatterns = [
    path('', RedirectView.as_view(url='/task'), name='redirect'),
    path('task/', TaskListView.as_view(),name='Task-list'),
    path('task/<int:pk>/' , TaskDetailView.as_view(), name="Task-detail"),
    path('task/create', TaskCreateView.as_view(), name='Task-create'),    
    path('task/<int:pk>/edit/', TaskEditView.as_view(), name='Task-edit'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='Task-delete'),
    path('task/<int:pk>/Done' , change_to_done , name='Task-done'),
    path('task/<int:pk>/Not_Done' , change_to_not_done , name='Task-not-done'),

]