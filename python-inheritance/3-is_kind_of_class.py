#!/usr/bin/python3
"""Module that defines a function to check class membership with inheritance"""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance of, or inherited from, the specified class

    Args:
        obj: the object to check
        a_class: the class to compare with

    Returns:
        True if obj is an instance of a_class or a subclass, False otherwise
    """
    return isinstance(obj, a_class)
