# views.py
from rest_framework import viewsets
from .models import Flight
from .serializers import FlightSerializer
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from typing import Any


class FlightViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Flight model.

    This ViewSet provides the CRUD operations for Flight model instances.

    Attributes:
        queryset (QuerySet): The queryset that should be used for this view.
        serializer_class (FlightSerializer): The serializer class to be used.

    Methods:
        create: Overrides the create method to handle ValidationErrors.
    """

    queryset: Any = Flight.objects.all()
    serializer_class: Any = FlightSerializer

    def create(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """
        Create a new Flight instance.

        This method overrides the default create method to handle ValidationErrors
        and return a custom response.

        Args:
            request (Any): The request object.
            *args (Any): Variable length argument list.
            **kwargs (Any): Arbitrary keyword arguments.

        Returns:
            Response: The response object.
        """
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
