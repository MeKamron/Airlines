from django.test import TestCase

from .models import Airplane
from .services import (calculate_total_fuel_consumption,
                       calculate_max_flight_length,
                       calculate_fuel_tank_capacity)


class AirplaneTestCase(TestCase):
    def setUp(self):
        Airplane.objects.create(id=10, num_of_passengers=200)
        Airplane.objects.create(id=12, num_of_passengers=400)

    def test_total_fuel_consumption(self) -> None:
        """
        Ensure total fuel consumption is calculated correctly
        """
        airplane1 = Airplane.objects.get(id=10)
        total_fuel_consumption1 = calculate_total_fuel_consumption(airplane1.id, airplane1.num_of_passengers)
        self.assertEqual(airplane1.total_fuel_consumption, total_fuel_consumption1)

        airplane2 = Airplane.objects.get(id=12)
        total_fuel_consumption2 = calculate_total_fuel_consumption(airplane2.id, airplane2.num_of_passengers)
        self.assertEqual(airplane2.total_fuel_consumption, total_fuel_consumption2)

    def test_max_flight_length_with_filled_tank(self) -> None:
        """
        Ensure maximum flight minutes is calculated correctly
        """
        airplane1 = Airplane.objects.get(id=10)
        total_fuel_consumption1 = calculate_total_fuel_consumption(airplane1.id, airplane1.num_of_passengers)
        max_flight_length1 = calculate_max_flight_length(calculate_fuel_tank_capacity(airplane1.id),
                                                         total_fuel_consumption1)
        self.assertEqual(airplane1.max_mins_to_fly, max_flight_length1)

        airplane2 = Airplane.objects.get(id=12)
        total_fuel_consumption2 = calculate_total_fuel_consumption(airplane2.id, airplane2.num_of_passengers)
        max_flight_length2 = calculate_max_flight_length(calculate_fuel_tank_capacity(airplane2.id),
                                                         total_fuel_consumption2)
        self.assertEqual(airplane2.max_mins_to_fly, max_flight_length2)

    def test_str_returns_id(self) -> None:
        """
        Ensure string representation of the instance object is its id
        """
        airplane1 = Airplane.objects.get(id=10)
        string_id = str(airplane1.id)
        self.assertEqual(str(airplane1), string_id)
