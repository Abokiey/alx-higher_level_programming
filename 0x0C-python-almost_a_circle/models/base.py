#!/usr/bin/python3

"""import modules"""

import json
import csv
import turtle

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """seriallize in csv"""
        file = "{}.csv".format(cls.__name__)

        if list_objs is None:
            return []
        with open(file, 'w', newline='') as f:
            writer = csv.writer(f)

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    data = [obj.id, obj.width, obj.height, obj.x, obj.y]
                if cls.__name__ == "Square":
                    data = [obj.id, obj.size, obj.x, obj.y]

                writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """deserialize in csv"""
        file = "{}.csv".format(cls.__name__)
        instances = []

        with open(file, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dictionary = {"id": int(row[0]),
                                  "width": int(row[1]),
                                  "height": int(row[2]),
                                  "x": int(row[3]),
                                  "y": int(row[4])}
                if cls.__name__ == "Square":
                    dictionary = {"id": int(row[0]),
                                  "size": int(row[1]),
                                  "x": int(row[2]),
                                  "y": int(row[3])}
                instance = cls.create(**dictionary)
                instances.append(instance)
            return (instances)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """open a window and draw all the
        rectangles and squares"""
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")

        turt = turtle.Turtle()
        turt.speed(2)

        for rect in list_rectangles:
            turt.penup()
            turt.goto(rect.x, rect.y)
            turt.pendown()
            turt.color("blue")
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)

        for sqr in list_squares:
            turt.penup()
            turt.goto(square.x, square.y)
            turt.pendown()
            turt.color("red")
            for j in range(4):
                turt.forward(square.size)
                turt.left(90)

        turt.hideturtle()
        screen.mainloop()
