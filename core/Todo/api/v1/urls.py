from django.urls import path, include
from .views import *
from rest_framework.routers import *

"""Using DefaultRouter to generate paths for views"""
router = DefaultRouter()
router.register("task", TaskModelViewSet, basename="task")
app_name = "api-v1"
urlpatterns = [path("weather", openweather, name="weather")]
urlpatterns += router.urls
