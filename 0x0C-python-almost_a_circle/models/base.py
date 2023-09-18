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

    @classmethod
    def save_to_file(cls, list_objs):
        """json string representation"""
        if list_objs is None:
            list_objs = []

        file = "{}.json".format(cls.__name__)

        with open(file, mode="w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dict))

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
        return (dummy_instance)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file = "{}.json".format(cls.__name__)
        new_list = []
        if file is None:
            return []

        try:
            with open(file, "r") as f:
                instances = cls.from_json_string(f.read())
            for i, dictionary in enumerate(instances):
                new_list.append(cls.create(**instances[i]))
            return new_list
        except IOError:
            return []

if __name__ == "__main__":
    from rectangle import Rectangle
    from square import Square

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file(list_squares_input)

    list_squares_output = Square.load_from_file()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))
