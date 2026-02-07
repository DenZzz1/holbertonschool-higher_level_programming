#!/usr/bin/python3
"""Module that defines a MyList class"""


class MyList(list):
    """MyList class that inherits from list

    Adds a method to print the list in sorted order
    """

    def print_sorted(self):
        """Print the list in ascending sorted order

        Does not modify the original list
        """
        print(sorted(self))
