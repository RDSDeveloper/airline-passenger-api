# serializers.py
from rest_framework import serializers
from .models import Flight
from airplanes.serializers import AirplaneSerializer
from airplanes.models import Airplane
from typing import Any


class FlightSerializer(serializers.ModelSerializer):
    """
    Serializer for the Flight model.

    This serializer is used to convert Flight model instances into JSON
    representations and vice versa. It defines the fields that should be
    included in the serialized output.

    Attributes:
        airplane_detail (Any): Serializer field for the airplane detail.
        airplane (Any): Serializer field for the airplane.

    Meta:
        model (Flight): The model class that the serializer is based on.
        fields (list[str]): The fields to include in the serialized output.
    """
    airplane_detail: Any = AirplaneSerializer(source="airplane", read_only=True)
    airplane: Any = serializers.PrimaryKeyRelatedField(queryset=Airplane.objects.all())

    class Meta:
        model = Flight
        fields: list[str] = [
            "departure_time",
            "arrival_time",
            "origin",
            "destination",
            "airplane",
            "airplane_detail",
        ]
