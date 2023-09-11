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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
