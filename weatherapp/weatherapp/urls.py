# weatherapp/urls.py
from django.urls import path, include

urlpatterns = [
    path('', include('weather.urls')),  # Includes all weather app URLs
]