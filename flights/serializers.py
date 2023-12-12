# serializers.py
from rest_framework import serializers
from .models import Flight
from airplanes.serializers import AirplaneSerializer
from airplanes.models import Airplane


class FlightSerializer(serializers.ModelSerializer):
    airplane_detail = AirplaneSerializer(source="airplane", read_only=True)
    airplane = serializers.PrimaryKeyRelatedField(queryset=Airplane.objects.all())

    class Meta:
        model = Flight
        fields = [
            "departure_time",
            "arrival_time",
            "origin",
            "destination",
            "airplane",
            "airplane_detail",
        ]
