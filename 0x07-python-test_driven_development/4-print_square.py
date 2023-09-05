#!/usr/bin/python3

def print_square(size):
    """prints the square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if size == 0:
        print("", end="")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
