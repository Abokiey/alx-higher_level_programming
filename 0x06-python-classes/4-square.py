#!/usr/bin/python3

"""class of a square"""


class Square:
    """initialize"""
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        """property setter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """property setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area of a square"""
        return (self.size ** 2)
