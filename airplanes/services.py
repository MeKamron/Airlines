"""
Note that calculations below are only applicable to
this application based on provided requirements.
"""
import math


def calculate_fuel_tank_capacity(airplane_id: int) -> int:
    return 200 * airplane_id


def calculate_total_fuel_consumption(airplane_id: int, num_of_passengers: int) -> float:
    base_fuel_consumption_per_minute = math.log(airplane_id) * 0.8
    passenger_increase = num_of_passengers * 0.0002
    total_fuel_consumption = base_fuel_consumption_per_minute + passenger_increase
    return round(total_fuel_consumption, 2)


def calculate_max_flight_length(fuel_tank_capacity: float, total_fuel_consumption_per_minute: float) -> float:
    result = fuel_tank_capacity / total_fuel_consumption_per_minute
    return round(result, 2)
