#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square

        Args:
            size: size of the square (default: 0)
            position: position of the square (default: (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size attribute

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute

        Args:
            value: new size value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position attribute

        Returns:
            The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position attribute

        Args:
            value: new position value

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square

        Returns:
            The area of the square (size * size)
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #

        If size is 0, print an empty line.
        Position is used to add spaces before and empty lines before the square.
        """
        if self.__size == 0:
            print()
        else:
            # Print vertical offset (position[1] empty lines)
            for i in range(self.__position[1]):
                print()
            # Print the square with horizontal offset (position[0] spaces)
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
