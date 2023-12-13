from django.db import models
from django.contrib.auth import get_user_model
from typing import Any


class Airplane(models.Model):
    id: int = models.AutoField(primary_key=True)
    user_defined_airplane_id: int = models.IntegerField()
    passenger_count: int = models.IntegerField(default=0)
    created_by: Any = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True
    )

    @property
    def fuel_tank_capacity(self) -> int:
        """
        Calculate the fuel tank capacity based on the user defined airplane id.
        Each unit of user_defined_airplane_id contributes 200 units to the fuel tank capacity.
        """
        return 200 * self.user_defined_airplane_id

    @property
    def fuel_consumption_per_minute(self) -> float:
        """
        Calculate the fuel consumption per minute.
        It's a function of the user_defined_airplane_id and the number of passengers.
        """
        return log(self.user_defined_airplane_id) * 0.80 + self.passenger_count * 0.002

    @property
    def max_minutes_to_fly(self) -> float:
        """
        Calculate the maximum minutes the airplane can fly.
        It's the ratio of the fuel tank capacity to the fuel consumption per minute.
        """
        return self.fuel_tank_capacity / self.fuel_consumption_per_minute

    def __str__(self) -> str:
        """
        Return a string representation of the airplane.
        """
        return f"Airplane {self.user_defined_airplane_id} with {self.passenger_count} passengers"
