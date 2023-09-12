#!/usr/bin/python3

"""json module"""

import json

"""writes object to text file"""


def save_to_json_file(my_obj, filename):
    """json representation"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
