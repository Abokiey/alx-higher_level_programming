#!/usr/bin/python3

"""Rectangle class"""


class Rectangle:
    """initialize"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter, returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter
        -> value - width value(int)
        -> raise TypeError - width must be an integer
        -> raise ValueError - width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """getter, returns height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter
        -> value - height(int)
        -> raise TypeError - height must be an integer
        -> raise ValueError - height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        "area of a rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """informal represantation of the object"""
        res = []
        string = ""
        if self.__height == 0 or self.__width == 0:
            return (string)
        for i in range(self.height):
            [res.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                res.append("\n")
        return ("".join(res))

    def __repr__(self) -> str:
        """Formal representation of the object"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """formatted deletion dunder del"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
