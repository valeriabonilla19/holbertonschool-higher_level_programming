#!/usr/bin/python3
"""
BaseGeometry class with area method and integer_validator method
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as an integer greater than 0

        Args:
            name (str): The name of the parameter
            value (any): The value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
