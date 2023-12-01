#!/usr/bin/python3
"""find the peak from a list of ints"""


def find_peak(list_of_integers):
    """find peak"""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    pk = list_of_integers[mid]
    if pk > list_of_integers[mid - 1] and pk > list_of_integers[mid + 1]:
        return pk
    elif pk < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])