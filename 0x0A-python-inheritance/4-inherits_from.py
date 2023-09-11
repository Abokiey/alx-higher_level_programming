#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    :if the object is an instance of a class that inherited
    :obj: object to check
    :a_class:the class to compare against
    :return: if the object is an instance of the class
    """
    return issubclass(type(obj), a_class)
