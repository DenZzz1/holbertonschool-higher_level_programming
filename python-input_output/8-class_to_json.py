#!/usr/bin/python3
"""Module that defines a function to convert class instance to dict"""


def class_to_json(obj):
    """Return dictionary description of an object for JSON serialization

    Args:
        obj: instance of a Class

    Returns:
        Dictionary with all serializable attributes
    """
    return obj.__dict__
