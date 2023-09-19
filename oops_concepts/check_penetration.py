#!/usr/bin/env python3


class ObstructionDetector:
  def __init__(self, location_a, location_b):
    self._location_a = location_a
    self._location_b = location_b

  @property
  def location_a(self):
    return self._location_a

  @location_a.setter
  def location_a(self, location_a):
    if not isinstance(location_a, list) or len(location_a) != 2:
      raise ValueError("location_a must be a list of two integers")

    self._location_a = location_a

  @property
  def location_b(self):
    return self._location_b

  @location_b.setter
  def location_b(self, location_b):
    if not isinstance(location_b, list) or len(location_b) != 2:
      raise ValueError("location_b must be a list of two integers")

    self._location_b = location_b

  def is_impenetrable(self):
    """Calculates if there is an impenetrable obstruction on the route from location_a to location_b.

    Returns:
      A boolean value, indicating whether or not there is an impenetrable obstruction on the route.
    """

    # Simulate the results of the time duration module.
    time_duration = random.randint(10, 120)

    # Calculate the expected time duration.
    distance = calculate_distance(self.location_a, self.location_b)
    speed = get_machine_speed()
    expected_time_duration = distance / speed

    # Compare the actual time duration to the expected time duration.
    if time_duration > expected_time_duration + 60:
      return True
    else:
      return False
