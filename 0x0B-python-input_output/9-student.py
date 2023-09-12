#!/usr/bin/python3

"""class student"""


class Student:
    """instantiation"""
    def __init__(self, first_name, last_name, age):
        self.first = first_name
        self.last = last_name
        self.age = age

    def to_json(self):
        """retrieves the dictionary representation"""
        return object.__dict__
