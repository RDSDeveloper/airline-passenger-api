# views.py
from rest_framework import viewsets
from .models import Flight
from .serializers import FlightSerializer
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ValidationError


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
