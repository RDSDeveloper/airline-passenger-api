from django.db import models
from airplanes.models import Airplane
from django.core.exceptions import ValidationError
from typing import Any


class Flight(models.Model):
    departure_time: Any = models.DateTimeField()
    arrival_time: Any = models.DateTimeField()
    origin: str = models.CharField(max_length=200)
    destination: str = models.CharField(max_length=200)
    airplane: Any = models.ForeignKey(Airplane, on_delete=models.CASCADE)

    def save(self, *args: Any, **kwargs: Any) -> None:
        """
        Save the flight.
        Raises a ValidationError if the departure time is not before the arrival time.
        """
        if self.departure_time >= self.arrival_time:
            raise ValidationError("Departure time must be before arrival time")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Return a string representation of the flight.
        """
        return (
            f"Flight from {self.origin} to {self.destination} on {self.departure_time}"
        )
