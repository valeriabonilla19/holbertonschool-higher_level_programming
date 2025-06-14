#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
It validates width and height and sets private attributes.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry and
    validates width and height as positive integers.
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
