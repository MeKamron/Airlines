import math

from django.db import models


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
        return 200 * self.id

    @property
    def base_fuel_consumption_per_minute(self) -> float:
        """
        How much fuel consumed per minute when flying without passengers
        """
        return math.log(self.id) * 0.8

    @property
    def total_fuel_consumption_per_minute(self) -> float:
        """
        Total amount of fuel consumed per minute with passengers
        (each passenger increases fuel consumption by 0.0002 litres)
        """
        passenger_increase = self.num_of_passengers * 0.0002
        return round(self.base_fuel_consumption_per_minute + passenger_increase, 2)

    @property
    def max_mins_to_fly(self) -> float:
        """
        Number of minutes airplane can fly with full tank and full passengers
        """
        result = self.fuel_tank_capacity / self.total_fuel_consumption_per_minute
        return round(result, 2)
