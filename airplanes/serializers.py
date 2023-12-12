from rest_framework import serializers
from .models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = [
            "id",
            "passenger_count",
            "fuel_tank_capacity",
            "fuel_consumption_per_minute",
        ]
