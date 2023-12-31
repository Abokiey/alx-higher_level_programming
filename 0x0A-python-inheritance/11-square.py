#!/usr/bin/python3

"""Square module"""
Rectangle = __import__('9-rectangle').Rectangle

"""square sub class"""


class Square(Rectangle):
    """class of a square"""
    def __init__(self, size):
        """initialization"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """dunder method"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
