#!/usr/bin/python3

"""import modules"""
import unittest
from rectangle import Rectangle
from base import Base


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(5, 10, 1, 2, 7)
        self.r2 = Rectangle(3, 6, 0, 0, 8)

    def test_area(self):
        self.assertEqual(self.r1.area(), 50)
        self.assertEqual(self.r2.area(), 18)

    def test_str(self):
        expected_r1 = "[rectangle] (7) 1/2 - 5/10"
        expected_r2 = "[rectangle] (8) 0/0 - 3/6"
        actual_r1 = str(self.r1)
        actual_r2 = str(self.r2)
        self.assertEqual(expected_r1, actual_r1)
        self.assertEqual(expected_r2, actual_r2)


    def test_update_args(self):
        expected_r1 = "[rectangle] (9) 3/1 - 4/7"
        self.r1.update(9, 4, 7, 3, 1)
        actual_r1 = str(self.r1)
        self.assertEqual(expected_r1, actual_r1)

    def test_update_kwargs(self):
        self.r2.update(id=5, width=2, height=4, x=1, y=2)
        self.assertEqual(str(self.r2), "[rectangle] (5) 1/2 - 2/4")


    def test_to_dictionary(self):
        r1_dict = self.r1.to_dictionary()
        self.assertEqual(r1_dict, {'id': 7, 'width': 5, 'height': 10, 'x': 1, 'y': 2})
        r2_dict = self.r2.to_dictionary()
        self.assertEqual(r2_dict, {'id': 8, 'width': 3, 'height': 6, 'x': 0, 'y': 0})


if __name__ == "__main__":
    unittest.main()
