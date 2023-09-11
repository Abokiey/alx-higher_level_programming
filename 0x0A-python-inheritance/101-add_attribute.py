#!/usr/bin/python3

"""add new attribute to an object"""



def add_attribute(obj, att, value):
    """add attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
