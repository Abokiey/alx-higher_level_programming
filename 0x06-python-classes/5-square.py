#!/usr/bin/python3
import sys

"""class of a square"""


class Square:
    """initialize"""
    def __init__(self, size=0):
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
        return (self.__size ** 2)

    def my_print(self):
        """prints the # character"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
