from rest_framework import serializers
from .models import Airplane
from typing import Any


class AirplaneSerializer(serializers.ModelSerializer):
    """
    Serializer for the Airplane model.

    This serializer is used to convert Airplane model instances into JSON
    representations and vice versa. It defines the fields that should be
    included in the serialized output.

    Attributes:
        fuel_consumption_per_minute (Any): Serializer field for the fuel consumption per minute.
        max_minutes_to_fly (Any): Serializer field for the maximum minutes to fly.

    Meta:
        model (Airplane): The model class that the serializer is based on.
        fields (list[str]): The fields to include in the serialized output.
    """

    fuel_consumption_per_minute: Any = serializers.FloatField(read_only=True)
    max_minutes_to_fly: Any = serializers.FloatField(read_only=True)

    class Meta:
        model = Airplane
        fields: list[str] = [
            "id",
            "user_defined_airplane_id",
            "passenger_count",
            "fuel_tank_capacity",
            "fuel_consumption_per_minute",
            "max_minutes_to_fly",
        ]
