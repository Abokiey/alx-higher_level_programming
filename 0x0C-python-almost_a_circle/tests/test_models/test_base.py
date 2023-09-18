#!/usr/bin/python3

"""unittest for base model"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestShapes(unittest.TestCase):

    def setUp(self):
        """Creating test data"""
        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)
        self.list_rectangles_input = [self.r1, self.r2]

        self.s1 = Square(5)
        self.s2 = Square(7, 9, 1)
        self.list_squares_input = [self.s1, self.s2]

    def tearDown(self):
        """ Cleaning up created files"""
        for cls in [Rectangle, Square]:
            json_file = "{}.json".format(cls.__name__)
            csv_file = "{}.csv".format(cls.__name__)
            if os.path.exists(json_file):
                os.remove(json_file)
            if os.path.exists(csv_file):
                os.remove(csv_file)

    def test_save_to_file_csv_and_load_from_file_csv(self):
        """Test saving and loading from CSV
        files for the Rectangle and Square
        """
        Rectangle.save_to_file_csv(self.list_rectangles_input)
        Square.save_to_file_csv(self.list_squares_input)

        loaded_rectangles = Rectangle.load_from_file_csv()
        loaded_squares = Square.load_from_file_csv()

        self.assertEqual(len(loaded_rectangles), len(self.list_rectangles_input))
        self.assertEqual(len(loaded_squares), len(self.list_squares_input))


if __name__ == "__main__":
    unittest.main()
