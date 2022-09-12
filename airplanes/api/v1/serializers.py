from rest_framework import serializers

from airplanes.models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ['id', 'num_of_passengers']


class ReadAirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ['id', 'total_fuel_consumption', 'max_mins_to_fly']
