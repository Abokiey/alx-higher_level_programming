#!/usr/bin/python3

"""inserts a line of text"""


def append_after(filename="", search_string="", new_string=""):
    """appending a line"""
    res = ""

    with open(filename, 'r') as file:
        for readline in file:
            res += readline
            if search_string in readline:
                res += new_string

    with open(filename, "w") as file:
        file.write(res)


if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
