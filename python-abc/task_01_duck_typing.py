#!/usr/bin/python3
"""
Defines Shape abstract class and concrete Circle and Rectangle classes
with area and perimeter methods, plus a duck-typing based shape_info function.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape class."""

    def __init__(self, radius):
        """
        Initialize Circle with radius.

        Args:
            radius (float or int): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape class."""

    def __init__(self, width, height):
        """
        Initialize Rectangle with width and height.

        Args:
            width (float or int): Width of the rectangle.
            height (float or int): Height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of a shape using duck typing.

    Args:
        shape (Shape): Instance of Shape or compatible class.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
