#!/usr/bin/python3

"""LockedClass"""


class LockedClass:
    """instantiation"""
    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)
