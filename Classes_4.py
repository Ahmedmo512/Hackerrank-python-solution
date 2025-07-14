# Vehicle Classes Problem 
#
# This problem requires implementing two vehicle classes: Car and Boat.
# Each class should store its maximum speed and return a specific string
# representation when printed.

# Class Car:
#   - Constructor takes two arguments:
#       1. max_speed (int)
#       2. speed_unit (str): either "km/h" or "mph"
#   - __str__ method returns:
#       "Car with the maximum speed of {max_speed} {speed_unit}"

# Class Boat:
#   - Constructor takes one argument:
#       1. max_speed (int)
#   - __str__ method returns:
#       "Boat with the maximum speed of {max_speed} knots"


class Car:
    def __init__(self, max_speed, speed_unit):
        self.max_speed = max_speed
        self.speed_unit = speed_unit

    def __str__(self):
        return f"Car with the maximum speed of {self.max_speed} {self.speed_unit}"

class Boat:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def __str__(self):
        return f"Boat with the maximum speed of {self.max_speed} knots"


car = Car(120, "km/h")
print(car)  # Car with the maximum speed of 120 km/h


boat = Boat(82)
print(boat)   # Boat with the maximum speed of 82 knots
