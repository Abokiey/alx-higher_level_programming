#!/usr/bin/python3

"""subclass mylist"""


class MyList(list):
    """prints a sorted list"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
