#!/usr/bin/python3

"""square of a number"""
class Square:

    """initialize"""
    def __init__(self, size=0):

        """conditions"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """area method"""
    def area(self):
        """area of square"""
        self.area = self.__size ** 2
        return (self.area)
