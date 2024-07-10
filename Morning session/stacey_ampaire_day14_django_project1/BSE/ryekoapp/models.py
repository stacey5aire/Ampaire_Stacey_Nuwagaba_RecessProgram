from django.db import models
from django.utils import timezone
# Create your models here.
class SoilMoistureReading(models.Model):
    #store timestamp of our reading with the default value of the current time we have
  timestamp = models.DateTimeField(default=timezone.now)
  moisture_level = models.FloatField()

def __str__(self):
   return f"{self.timestamp} - {self.moisture_level}" 