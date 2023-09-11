#!/usr/bin/python3

"""instancr of an object"""


def is_kind_of_class(obj, a_class):
    """
    checks if the object is an instaance of or an\
            instance of a class
    :obj: The object to check.
    :a_class: The class to compare against.
    :return: True if obj is an instance of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
