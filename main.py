class Vehicle:
    """A simple class representing a vehicle.

    This class allows users to create a vehicle, and also compare vehicles by speed

    Attributes:
        - model (str): The name of the vehicle
        - speed (int): The speed of the vehicle
        - cost (int): The cost of the vehicle

    Methods:
        - __init__(self): Initializes the new vehicle with given attributes
        - __gt__(self): Returns true if the vehicle`s speed greater than other speed
        - __repr__(self): Returns a string representation of the vehicle

    Example usage:
    >>> vehicle_2 = Vehicle('Mitsubishi', 200, 23800)
    >>> vehicle_1 = Vehicle('Ford', 180, 22800)
    >>> vehicle_3 = Vehicle('Lexus', 230, 44800)
    >>> example_result = sorted([vehicle_2, vehicle_1, vehicle_3])
    >>> print(result)
    [Ford: speed = 180, cost = 22800, Mitsubishi: speed = 200, cost = 23800, Lexus: speed = 230, cost = 44800]
    >>> is_greater = vehicle_1 > vehicle_2
    >>> print(is_greater)
    False
    """

    def __init__(self, model, speed, cost):
        """Initializes a new vehicle with given model, speed and cost."""
        self.model = model
        self.speed = speed
        self.cost = cost

    def __gt__(self, other):
        """Returns true if the vehicle`s speed is greater than other speed."""
        if not isinstance(other, self.__class__):
            raise TypeError('Objects should be instances of Vehicle class')

        return self.speed > other.speed

    def __repr__(self):
        """Returns a string representation of the vehicle"""
        return f'{self.model}: speed = {self.speed}, cost = {self.cost}'


v_2 = Vehicle('Mitsubishi', 200, 23800)
v_1 = Vehicle('Ford', 180, 22800)
v_3 = Vehicle('Lexus', 230, 44800)

result = sorted([v_2, v_1, v_3])
print(result)
