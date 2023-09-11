#!/usr/bin/python3

"""class inheritance"""


def inherits_from(obj, a_class):
    """
    :if the object is an instance of a class that inherited
    :obj: object to check
    :a_class:the class to compare against
    :return: if the object is an instance of the class
    """
    if getattr(obj, "__class__") == a_class:
        return False
    return isinstance(obj, a_class)
