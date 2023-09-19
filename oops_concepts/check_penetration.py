#!/usr/bin/env python3


"""

Module to check for obstruction between two points
Usage:
obstruction = ObstructionDetector([1.2, 2.4], [4.5, 6.7]).is_impenetrable
"""

import random


class ObstructionDetector:
    def __init__(self, location_a, location_b):
        self._location_a = location_a
        self._location_b = location_b

    @property
    def location_a(self):
        return self._location_a

    @location_a.setter
    def location_a(self, location_a: list) -> None:
        """
        Set location_b
        Args:
            location_a (list): List of floats
        """
        if not isinstance(location_a, list) or len(location_a) != 2:
            raise ValueError("Invalid co-ordinates")

        self._location_a = location_a

    @property
    def location_b(self):
        return self._location_b

    @location_b.setter
    def location_b(self, location_b: list) -> None:
        """
        Set location_b
        Args:
            location_b (list): List of floats
        """
        if not isinstance(location_b, list) or len(location_b) != 2:
            raise ValueError("location_b must be a list of two integers")

        self._location_b = location_b

    
    def  calculate_distance(self):
        return abs(location_a[0] - location_b[0]) + abs(location_a[1] - location_b[1])

    def is_impenetrable(self, speed: int) -> bool:
        """
        Determine if there's an obstruction
        Args:
            speed (int): Speed of the machine used
        """
        # simulate the time 
        time_duration = random.randint(10, 120)

        distance = calculate_distance(self.location_a, self.location_b)
        expected_time_duration = distance / speed

        return (time_duration > expected_time_duration + 60)
