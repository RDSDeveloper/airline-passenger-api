from django.test import TestCase
from .models import Airplane
from math import log


class AirplaneModelTest(TestCase):
    def setUp(self):
        self.airplane = Airplane.objects.create(passenger_count=100)

    def test_fuel_tank_capacity(self):
        expected_capacity = 200 * self.airplane.id
        self.assertEqual(self.airplane.fuel_tank_capacity, expected_capacity)

    def test_fuel_consumption_per_minute(self):
        expected_consumption = (
            log(self.airplane.id) * 0.80 + self.airplane.passenger_count * 0.002
        )
        self.assertEqual(
            self.airplane.fuel_consumption_per_minute, expected_consumption
        )
