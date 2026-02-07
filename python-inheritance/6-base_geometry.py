#!/usr/bin/python3
"""Module that defines a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class with area method"""

    def area(self):
        """Calculate the area

        Raises:
            Exception: always raises with message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")
