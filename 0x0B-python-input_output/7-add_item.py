#!/usr/bin/python3

"""import modules"""
from sys import argv
import json


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


file = "add_item.json"

try:
    json_list = load_from_json_file(file)
except FileNotFoundError:
    json_list = []

for arg in argv[1:]:
    json_list.append(arg)

save_to_json_file(json_list, file)
