#!/usr/bin/python3
"""Module that defines a function to check inheritance"""


def inherits_from(obj, a_class):
    """Check if object is an instance of a class that inherited from a_class

    Args:
        obj: the object to check
        a_class: the class to compare with

    Returns:
        True if obj's class inherited (directly or indirectly) from a_class
        False if obj is exactly an instance of a_class or not related
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
