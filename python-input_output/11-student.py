#!/usr/bin/python3
"""
Defines a Student class with methods to
serialize to JSON and reload from JSON.
"""


class Student:
    """
    Student class with public attributes and
    methods to serialize and reload attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): First name of student.
            last_name (str): Last name of student.
            age (int): Age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student.

        If attrs is a list of strings, only include those attributes.

        Args:
            attrs (list, optional): List of attribute names to include.

        Returns:
            dict: Dictionary of attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance from a dictionary.

        Args:
            json (dict): Dictionary of attributes to update.
        """
        for key, value in json.items():
            setattr(self, key, value)
