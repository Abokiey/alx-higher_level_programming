#!/usr/bin/python3

"""max_integer([]) function unittest"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class Test_Max_Integer(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -2, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -3, 0, 4, -2]), 4)

    def test_floats(self):
        self.assertAlmostEqual(max_integer([1.5, 3.7, 2.1]), 3.7)

    def test_single_element(self):
        self.assertEqual(max_integer([12]), 12)

    def test_string_number_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key': 1, 'key1': 2})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)


