#!/usr/bin/python3
"""Module that defines a function to save object to JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation

    Args:
        my_obj: object to serialize to JSON
        filename: name of the file to write to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
