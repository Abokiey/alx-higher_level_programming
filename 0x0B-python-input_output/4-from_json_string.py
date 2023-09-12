#!/usr/bin/python3

"""json module"""

import json

"""converts from json str to py. object"""


def from_json_string(my_str):
    """deserialization from json str"""
    return (json.loads(my_str))
