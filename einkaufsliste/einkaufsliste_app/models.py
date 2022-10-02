from datetime import datetime
from django.db import models

# Create your models here.

class PurchasingItem(models.Model):
    name = models.CharField(max_length=70)
    is_active = models.BooleanField(default=True)

class CustomList(models.Model):
    name = models.CharField(max_length=70)

class ListItem(models.Model):
    name = models.CharField(max_length=140)
    custom_list = models.ForeignKey(CustomList, on_delete=models.CASCADE)

class WeatherData(models.Model):
    CURRENT_WEATHER = 1
    FORECAST_WEATHER = 2
    DATA_TYPE_CHOICES = [
        (CURRENT_WEATHER, 'current weather'),
        (FORECAST_WEATHER, 'forecast weather')
    ]
    data_type = models.PositiveSmallIntegerField(choices=DATA_TYPE_CHOICES)
    weather_id = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=140)
    temperature = models.DecimalField(max_digits=6, decimal_places=2)
    temperature_min = models.DecimalField(max_digits=6, decimal_places=2)
    temperature_max = models.DecimalField(max_digits=6, decimal_places=2)
    clouds = models.PositiveSmallIntegerField()
    weather_date = models.DateTimeField()
    data_received_date = models.DateTimeField()
    probability_of_rain = models.DecimalField(max_digits=4, decimal_places=2, null=True, default=None, blank=True)

class WasteEvent(models.Model):
    name = models.CharField(max_length=140)
    event_date = models.DateField()

    class Meta:
        ordering = ['event_date']