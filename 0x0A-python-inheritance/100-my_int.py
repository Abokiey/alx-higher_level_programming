#!/usr/bin/python3

"""myint subclass"""


class MyInt(int):
    """myint class"""
    def __eq__(self, __value: object):
        """inverted == """
        return not super().__eq__(__value)

    def __ne__(self, __value: object):
        """inverted != """
        return not super().__ne__(__value)
