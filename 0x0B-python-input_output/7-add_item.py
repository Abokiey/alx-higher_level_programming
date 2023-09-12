#!/usr/bin/python3

"""import modules"""
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


file = "add_item.json"
lists = []

with open(file, 'a') as f:
    pass

with open(file, 'r') as f:
    data = f.read()
    if data != "":
        lists = load(file)

    lists += sys.argv[1:]
    save_to_json_file(lists, file)
