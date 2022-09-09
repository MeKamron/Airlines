from rest_framework import viewsets
from rest_framework.decorators import action

from airplanes.models import Airplane

from airplanes.api.v1.serializers import AirplaneSerializer, ReadAirplaneSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ReadAirplaneSerializer
        return AirplaneSerializer
