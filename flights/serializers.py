# serializers.py
from rest_framework import serializers
from .models import Flight
from airplanes.serializers import AirplaneSerializer

class FlightSerializer(serializers.ModelSerializer):
    airplane = AirplaneSerializer(read_only=True)

    class Meta:
        model = Flight
        fields = ["departure_time", "arrival_time", "origin", "destination", "airplane"]
