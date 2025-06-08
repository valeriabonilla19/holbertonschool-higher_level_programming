#!/usr/bin/python3
"""
Defines a Student class with public attributes and
a method to retrieve its dictionary representation.
"""


class Student:
    """
    Student class with first_name, last_name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the dictionary representation of the Student instance.

        Returns:
            dict: Dictionary with all instance attributes.
        """
        return self.__dict__.copy()
