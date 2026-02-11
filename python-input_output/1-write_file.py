#!/usr/bin/python3
"""Module that defines a function to write to a file"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return number of characters

    Args:
        filename: name of the file to write to (default: empty string)
        text: text to write to the file (default: empty string)

    Returns:
        The number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
