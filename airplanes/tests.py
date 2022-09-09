import math

from django.test import TestCase

from .models import Airplane


class AirplaneTestCase(TestCase):
    def setUp(self):
        Airplane.objects.create(id=10, num_of_passengers=200)
        Airplane.objects.create(id=12, num_of_passengers=400)

    def test_total_fuel_consumption_with_passengers(self) -> None:
        """
        Ensure total fuel consumption is calculated correctly
        """
        airplane1 = Airplane.objects.get(id=10)
        total_fuel_consumption = (math.log(airplane1.id) * 0.8) + (airplane1.num_of_passengers * 0.0002)
        rounded_total_fuel_consumption = round(total_fuel_consumption, 2)
        self.assertEqual(airplane1.total_fuel_consumption_per_minute, rounded_total_fuel_consumption)

        airplane2 = Airplane.objects.get(id=12)
        total_fuel_consumption2 = (math.log(airplane2.id) * 0.8) + (airplane2.num_of_passengers * 0.0002)
        rounded_total_fuel_consumption = round(total_fuel_consumption2, 2)
        self.assertEqual(airplane2.total_fuel_consumption_per_minute, rounded_total_fuel_consumption)

    def test_max_flight_length_with_filled_tank(self) -> None:
        """
        Ensure maximum flight minutes is calculated correctly
        """
        airplane1 = Airplane.objects.get(id=10)
        total_fuel_consumption = (math.log(airplane1.id) * 0.8) + (airplane1.num_of_passengers * 0.0002)
        rounded_total_fuel_consumption = round(total_fuel_consumption, 2)
        max_flight_length = (airplane1.id * 200) / rounded_total_fuel_consumption
        self.assertEqual(airplane1.max_mins_to_fly, round(max_flight_length, 2))

        airplane2 = Airplane.objects.get(id=12)
        total_fuel_consumption2 = (math.log(airplane2.id) * 0.8) + (airplane2.num_of_passengers * 0.0002)
        rounded_total_fuel_consumption = round(total_fuel_consumption2, 2)
        max_flight_length2 = (airplane2.id * 200) / rounded_total_fuel_consumption
        self.assertEqual(airplane2.max_mins_to_fly, round(max_flight_length2, 2))

    def test_str_returns_id(self) -> None:
        """
        Ensure string representation of the instance object is its id
        """
        airplane1 = Airplane.objects.get(id=10)
        string_id = str(airplane1.id)
        self.assertEqual(str(airplane1), string_id)
