# weather/urls.py
from django.urls import path
from . import views  # Make sure this import is correct

urlpatterns = [
    path('', views.current_weather, name='current_weather'),  # Must match function name
]