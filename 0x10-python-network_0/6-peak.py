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
    peak_no = list_of_integers[mid]
    if peak_no > list_of_integers[mid - 1] and peak_no > list_of_integers[mid + 1]:
        return peak_no
    elif peak_no < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
