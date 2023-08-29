#!/usr/bin/python3

"""class of a square"""


class Square:
    """initialize"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """property setter"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """property setter"""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            not all(i >= 0 for i in value)):

            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area of a square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints the # character"""
        if self.__size == 0:
            print("")
            return

        for _ in range(0, self.__position[1]):
            print("")

        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))
