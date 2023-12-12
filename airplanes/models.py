from django.db import models
from math import log
from django.contrib.auth import get_user_model


class Airplane(models.Model):
    id = models.AutoField(primary_key=True)
    passenger_count = models.IntegerField(default=0)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    @property
    def fuel_tank_capacity(self):
        return 200 * self.id

    @property
    def fuel_consumption_per_minute(self):
        return log(self.id) * 0.80 + self.passenger_count * 0.002

    def __str__(self):
        return f"Airplane {self.id} with {self.passenger_count} passengers"
