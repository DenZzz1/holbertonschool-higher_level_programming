#!/usr/bin/python3
"""Module that defines a function to load object from JSON file"""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file

    Args:
        filename: name of the JSON file to load

    Returns:
        Python object represented by the JSON file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
