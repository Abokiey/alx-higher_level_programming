#!/usr/bin/python3

def roman_to_int(roman_string):

    if not str or type(roman_string) is not str:
        return 0

    maps = {
        "M": 1000,
        "C": 100,
        "X": 10,
        "I": 1,
        "D": 500,
        "L": 50,
        "V": 5
    }

    def get_val(idx):
        return maps[roman_string[idx]]

    indx = 0
    sum = 0
    length = len(roman_string)
    while (indx < length):
        if (indx + 1 < length):
            if (get_val(indx) < get_val(indx + 1)):
                sum += (get_val(indx + 1) - get_val(indx))
                indx += 1
            else:
                sum += get_val(indx)
        else:
            sum += maps[roman_string[indx]]
        indx += 1

    return sum
