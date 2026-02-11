#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """Student class with first_name, last_name, and age attributes"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student

        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student instance

        Args:
            attrs: list of attribute names to retrieve (optional)
                   If None, retrieve all attributes

        Returns:
            Dictionary with specified attributes (or all if attrs is None)
        """
        if attrs is None:
            return self.__dict__

        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result
