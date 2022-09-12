from django.db import models

from .services import (calculate_total_fuel_consumption,
                       calculate_max_flight_length,
                       calculate_fuel_tank_capacity)


class Airplane(models.Model):
    id = models.PositiveIntegerField(unique=True, primary_key=True)
    num_of_passengers = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('-created_at', )

    @property
    def fuel_tank_capacity(self) -> int:
        return calculate_fuel_tank_capacity(self.id)

    @property
    def total_fuel_consumption(self) -> float:
        """
        Total amount of fuel consumed per minute with passengers
        (each passenger increases fuel consumption by certain number of litres)
        """
        return calculate_total_fuel_consumption(self.id, self.num_of_passengers)

    @property
    def max_mins_to_fly(self) -> float:
        """
        Number of minutes airplane can fly with full tank and full passengers
        """
        return calculate_max_flight_length(self.fuel_tank_capacity, self.total_fuel_consumption)
