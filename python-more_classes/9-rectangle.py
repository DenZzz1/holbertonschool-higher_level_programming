#!/usr/bin/python3
"""Module that defines a Rectangle class"""


class Rectangle:
    """Class that defines a rectangle

    Attributes:
        number_of_instances: number of Rectangle instances
        print_symbol: symbol used for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle

        Args:
            width: width of the rectangle (default: 0)
            height: height of the rectangle (default: 0)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width attribute

        Returns:
            The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute

        Args:
            value: new width value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute

        Returns:
            The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute

        Args:
            value: new height value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle

        Returns:
            The area of the rectangle (width * height)
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle

        Returns:
            The perimeter of the rectangle (2 * (width + height))
            Returns 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation of the rectangle

        Returns:
            String representation using print_symbol
            Empty string if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            rectangle.append(str(self.print_symbol) * self.__width)
        return "\n".join(rectangle)

    def __repr__(self):
        """Return official string representation of the rectangle

        Returns:
            String that can recreate the rectangle using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor - called when the rectangle instance is deleted

        Prints a farewell message and decrements the instance counter
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles and return the bigger one based on area

        Args:
            rect_1: first Rectangle instance
            rect_2: second Rectangle instance

        Returns:
            The rectangle with the bigger area, or rect_1 if equal

        Raises:
            TypeError: if rect_1 or rect_2 is not a Rectangle instance
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a new Rectangle instance with width == height == size

        Args:
            size: size of the square (default: 0)

        Returns:
            A new Rectangle instance with width == height == size
        """
        return cls(size, size)
