from django.db import models
from math import log


class Airplane(models.Model):
    id = models.AutoField(primary_key=True)
    passenger_count = models.IntegerField(default=0)

    @property
    def fuel_tank_capacity(self):
        return 200 * self.id

    @property
    def fuel_consumption_per_minute(self):
        return log(self.id) * 0.80 + self.passenger_count * 0.002
