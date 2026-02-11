#!/usr/bin/python3
"""Module that defines a function to convert object to JSON string"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string)

    Args:
        my_obj: object to serialize to JSON

    Returns:
        JSON string representation of the object
    """
    return json.dumps(my_obj)
