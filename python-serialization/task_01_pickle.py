#!/usr/bin/python3
"""
Module for serializing and deserializing a custom object using pickle.
"""

import pickle


class CustomObject:
    """
    A custom class with name, age, and is_student attributes.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a new CustomObject.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the object's attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object to a file using pickle.

        Args:
            filename (str): The name of the file to serialize to.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            pass

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file using pickle.

        Args:
            filename (str): The name of the file to deserialize from.

        Returns:
            CustomObject or None: The deserialized object or None on failure.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                return None
        except (FileNotFoundError, pickle.UnpicklingError):
            return None
