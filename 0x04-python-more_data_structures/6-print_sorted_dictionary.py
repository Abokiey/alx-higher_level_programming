#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    i = sorted(a_dictionary.keys())

    for element in i:
        print("{}: {}".format(element, a_dictionary.get(element)))
