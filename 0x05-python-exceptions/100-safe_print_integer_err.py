#!/usr/bin/python
import sys


def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return (False)


if __name__ == "__main__":
    value = 89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "School"
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
