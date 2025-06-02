#!/usr/bin/python3
"""
BaseGeometry class with an area method that raises an Exception
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception because area is not implemented"""
        raise Exception("area() is not implemented")
