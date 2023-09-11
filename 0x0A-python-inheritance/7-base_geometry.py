#!/usr/bin/python3

"""base class"""


class BaseGeometry:
    """base geometry class"""

    def area(self):
        """implimentation of area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if value is int
        :name: name
        :value: int
        :raises TypeError: <name> must be an integer
        :raises ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
