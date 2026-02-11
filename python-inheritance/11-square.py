#!/usr/bin/python3
"""Module that defines a Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a new Square

        Args:
            size: size of the square (must be a positive integer)
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return string representation of the square

        Returns:
            String in format [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
