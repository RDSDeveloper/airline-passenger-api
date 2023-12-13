from rest_framework import serializers
from .models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):
    fuel_consumption_per_minute = serializers.FloatField(read_only=True)
    max_minutes_to_fly = serializers.FloatField(read_only=True)

    class Meta:
        model = Airplane
        fields = [
            "id",
            "user_defined_airplane_id",
            "passenger_count",
            "fuel_tank_capacity",
            "fuel_consumption_per_minute",
            "max_minutes_to_fly",
        ]