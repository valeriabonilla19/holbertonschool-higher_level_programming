#!/usr/bin/python3
"""
Defines a Student class with public attributes and
a to_json method that can filter attributes.
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

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the Student instance.
        If attrs is a list of strings, only attributes in this list are included.

        Args:
            attrs (list, optional): List of attribute names to retrieve.

        Returns:
            dict: Dictionary with selected instance attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__.copy()
