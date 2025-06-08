#!/usr/bin/python3
"""
Defines a CustomObject class with serialization
and deserialization using pickle.
"""

import pickle


class CustomObject:
    """
    A class representing a custom object with
    name, age, and is_student attributes.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes the CustomObject instance.

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
        Prints the attributes of the object in a formatted manner.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serializes the object and saves it to the given filename.

        Args:
            filename (str): The name of the file to save to.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            pass  # Silently ignore exceptions as per instruction

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from the given filename.

        Args:
            filename (str): The name of the file to load from.

        Returns:
            CustomObject: The loaded object, or None if error occurs.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
        except Exception:
            pass
        return None
