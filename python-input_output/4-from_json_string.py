#!/usr/bin/python3
"""Module that defines a function to convert JSON string to object"""
import json


def from_json_string(my_str):
    """Return an object (Python data structure) from a JSON string

    Args:
        my_str: JSON string to deserialize

    Returns:
        Python object represented by the JSON string
    """
    return json.loads(my_str)
