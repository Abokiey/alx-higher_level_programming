#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniques = set(my_list)
    n = 0

    for i in uniques:
        n += i
    return (n)
