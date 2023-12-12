# serializers.py
from rest_framework import serializers
from .models import Flight


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["departure_time", "arrival_time", "origin", "destination", "airplane"]
