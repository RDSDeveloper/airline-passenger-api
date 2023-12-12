from django.test import TestCase
from django.utils import timezone
from airplanes.models import Airplane
from .models import Flight
from django.core.exceptions import ValidationError


class FlightModelTest(TestCase):
    def setUp(self):
        self.airplane = Airplane.objects.create(passenger_count=100)
        self.flight = Flight.objects.create(
            departure_time=timezone.now(),
            arrival_time=timezone.now() + timezone.timedelta(hours=2),
            origin="New York",
            destination="London",
            airplane=self.airplane,
        )

    def test_str(self):
        expected_str = f"Flight from {self.flight.origin} to {self.flight.destination} on {self.flight.departure_time}"
        self.assertEqual(str(self.flight), expected_str)

    def test_departure_time_must_be_before_arrival_time(self):
        with self.assertRaises(ValidationError):
            Flight.objects.create(
                departure_time=timezone.now(),
                arrival_time=timezone.now() - timezone.timedelta(hours=2),
                origin="New York",
                destination="London",
                airplane=self.airplane,
            )
