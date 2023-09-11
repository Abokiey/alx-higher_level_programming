#!/usr/bin/python3

"""base class"""


class BaseGeometry:
    """base geometry class"""

    def area(self):
        """implimentation of area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if value is int"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
