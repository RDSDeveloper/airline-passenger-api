from rest_framework import viewsets
from .models import Airplane
from .serializers import AirplaneSerializer
from typing import Any


class AirplaneViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Airplane model.

    This ViewSet provides the CRUD operations for Airplane model instances.

    Attributes:
        queryset (QuerySet): The queryset that should be used for this view.
        serializer_class (AirplaneSerializer): The serializer class to be used.
    """

    queryset: Any = Airplane.objects.all()
    serializer_class: Any = AirplaneSerializer
