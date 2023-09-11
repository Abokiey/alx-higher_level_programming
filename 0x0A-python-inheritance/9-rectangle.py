#!/usr/bin/python3

    """rectangle module"""


    BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""rectangle class"""



class Rectangle(BaseGeometry):
    """subclass rectangle"""
    def __init__(self, width, height):
        """instantiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculate the area of the triangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """dunder method"""
        print("{} {}/{}".format([Rectangle], self.__width, self.__height))
