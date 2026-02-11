#!/usr/bin/env python3
"""
Custom object serialization module using pickle
"""
import pickle


class CustomObject:
    """
    Custom object with name, age, and is_student attributes
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject

        Args:
            name: string - name of the person
            age: integer - age of the person
            is_student: boolean - whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle

        Args:
            filename: name of the file to save the serialized object
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Error during serialization: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle

        Args:
            filename: name of the file containing the serialized object

        Returns:
            CustomObject instance or None if error occurs
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError) as e:
            print(f"Error during deserialization: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
