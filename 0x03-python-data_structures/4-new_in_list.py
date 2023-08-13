#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    list_cpy = my_list[:]

    elem_no = len(list_cpy)
    if idx < 0:
        return list_cpy
    if idx >= elem_no:
        return list_cpy
    list_cpy[idx] = element
    return list_cpy
