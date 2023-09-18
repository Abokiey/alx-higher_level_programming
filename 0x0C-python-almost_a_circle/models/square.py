#!/usr/bin/python3

"""import module"""

from models.rectangle import Rectangle

"""square subclass"""


class Square(Rectangle):
    """instantiation"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size of equal width and height"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """dunder method"""
        return ("[square] ({}) {}/{} - {}".format(self.id,
                                                  self.x,
                                                  self.y,
                                                  self.size))

    def update(self, *args, **kwargs):
        """assign attributes"""
        if args:
            keys = ["id", "size", "x", "y"]
            for key, value in zip(keys, args):
                setattr(self, key, value)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ representation of a Square in a dict"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }


if __name__ == "__main__":

    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)
