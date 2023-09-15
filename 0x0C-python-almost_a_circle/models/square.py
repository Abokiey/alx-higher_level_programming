#!/usr/bin/python3

"""import module"""

from rectangle import Rectangle

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
        return ("[square] ({}) {}/{} - {}".format(self.id, self.x,
            self.y, self.size))

    def update(self, *args, **kwargs):
        """assign attributes"""
        if args:
            keys = ["id", "size", "x", "y"]
            for key, value in zip(keys, args):
                setattr(self, key, value)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)


if __name__ == "__main__":

    s1 = Square(5)
    print(s1)

    s1.update(10)
    print(s1)

    s1.update(1, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

    s1.update(size=7, id=89, y=1)
    print(s1)
