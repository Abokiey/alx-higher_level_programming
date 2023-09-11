#!/usr/bin/python3

"""instance of an object"""


def is_same_class(obj, a_class):
    """
    :Check if an object is exactly an instance of the specified class.
    :obj: The object to check.
    :a_class: The class to compare against.
    :return: True if obj is an instance of a_class, otherwise False.
    """
    return getattr(obj, "__class__") is a_class
