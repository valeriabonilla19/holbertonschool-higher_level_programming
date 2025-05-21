#!/usr/bin/python3
"""Module 1-square
Defines a class Square with a private instance attribute.
"""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initializes the square with a private size.

        Args:
            size: The size of the square.
        """
        self.__size = size
