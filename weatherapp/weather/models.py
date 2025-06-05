# weather/models.py (only if you need database storage)
from django.db import models

class WeatherCache(models.Model):
    location = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=200)
    last_updated = models.DateTimeField(auto_now=True)