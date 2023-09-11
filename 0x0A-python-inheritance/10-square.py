#!/usr/bin/python3

"""Square module"""
Rectangle = __import__('9-rectangle').Rectangle

"""square sub class"""


class Square(Rectangle):
    """class of a square"""
    def __init__(self, size):
        """initialization"""
        super().__init__(size, size)
