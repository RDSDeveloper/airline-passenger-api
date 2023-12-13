from django.db import models
from airplanes.models import Airplane
from django.core.exceptions import ValidationError


class Flight(models.Model):
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.departure_time >= self.arrival_time:
            raise ValidationError("Departure time must be before arrival time")
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"Flight from {self.origin} to {self.destination} on {self.departure_time}"
        )
