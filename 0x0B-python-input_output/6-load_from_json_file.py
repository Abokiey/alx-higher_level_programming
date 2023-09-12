#!/usr/bin/python3

"""import module"""

import json

"""create an object"""


def load_from_json_file(filename):
    """json deserialization"""
    with open(filename, 'r', encoding="utf-8")as f:
        return f.read(json.loads(filename))
