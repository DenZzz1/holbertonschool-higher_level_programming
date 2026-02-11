#!/usr/bin/python3
"""Module that defines a function to append to a file"""


def append_write(filename="", text=""):
    """Append a string at the end of a text file (UTF8)

    Args:
        filename: name of the file to append to (default: empty string)
        text: text to append to the file (default: empty string)
 
    Returns:
        The number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
