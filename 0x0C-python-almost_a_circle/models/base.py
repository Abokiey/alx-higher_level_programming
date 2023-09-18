#!/usr/bin/python3

"""import modules"""

import json

"""base model class"""


class Base:
    """instantiation"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """serialize to json string"""
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        class_name = list_dictionaries[0].__class__.__name__
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """save to file from json string"""
        if list_objs is None:
            list_objs = []

        file = "{}.json".format(cls.__name__)
        with open(file, 'w', encoding='utf-8') as f:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the json string"""
        if json_string is None:
            return ("[]")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create an instance with all attributes"""
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
            dummy_instance.update(**dictionary)
        else:
            dummy_instance = cls(1)
            dummy_instance.update(**dictionary)
        return dummy_instance


if __name__ == "__main__":
    from rectangle import Rectangle

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
