#!/usr/bin/python3
"""json module"""

import json

"""json representation of a string"""


def to_json_string(my_obj):
    """serialize file to json string"""
    return json.dumps(my_obj)
