from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Airplane
from math import log


class AirplaneModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.airplane = Airplane.objects.create(
            passenger_count=100, created_by=self.user
        )

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

    def test_max_minutes_to_fly(self):
        expected_minutes = (
            self.airplane.fuel_tank_capacity / self.airplane.fuel_consumption_per_minute
        )
        self.assertEqual(self.airplane.max_minutes_to_fly, expected_minutes)

    def test_str(self):
        expected_str = f"Airplane {self.airplane.id} with {self.airplane.passenger_count} passengers"
        self.assertEqual(str(self.airplane), expected_str)

    def test_created_by(self):
        self.assertEqual(self.airplane.created_by, self.user)
