#!/usr/bin/python3

"""class student"""


class Student:
    """instantiation"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves the dictionary representation"""
        if attrs is None:
            return (self.__dict__)
        else:
            dictionary = {}
            for at in attrs:
                if at in self.__dict__.keys():
                    dictionary[at] = self.__dict__[at]
            return (dictionary)

    def reload_from_json(self, json):
        """replaces attrs of the student instance"""
        for key, value in json.items():
            setattr(self, key, value)
