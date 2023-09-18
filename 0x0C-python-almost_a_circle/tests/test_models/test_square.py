#!/usr/bin/python3

"""import modules"""

import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):

    def setUp(self):
        self.s1 = Square(5, 1, 2, 7)
        self.s2 = Square(3, 0, 0, 8)

    def test_size_property(self):
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s2.size, 3)

    def test_size_setter(self):
        self.s1.size = 8
        self.assertEqual(self.s1.size, 8)
        self.assertEqual(self.s1.width, 8)
        self.assertEqual(self.s1.height, 8)

    def test_str(self):
        expected_s1 = "[square] (7) 1/2 - 5"
        expected_s2 = "[square] (8) 0/0 - 3"
        self.assertEqual(str(self.s1), expected_s1)
        self.assertEqual(str(self.s2), expected_s2)

    def test_update_args(self):
        self.s1.update(9, 4, 1, 2)
        self.assertEqual(str(self.s1), "[square] (9) 1/2 - 4")

    def test_update_kwargs(self):
        self.s2.update(id=5, size=2, x=1, y=2)
        self.assertEqual(str(self.s2), "[square] (5) 1/2 - 2")

    def test_to_dictionary(self):
        s1_dict = self.s1.to_dictionary()
        self.assertEqual(s1_dict, {'id': 7, 'size': 5, 'x': 1, 'y': 2})
        s2_dict = self.s2.to_dictionary()
        self.assertEqual(s2_dict, {'id': 8, 'size': 3, 'x': 0, 'y': 0})


if __name__ == "__main__":
    unittest.main()
