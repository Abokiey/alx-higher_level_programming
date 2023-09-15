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


if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
