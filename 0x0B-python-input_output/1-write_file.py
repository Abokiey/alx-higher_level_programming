#!/usr/bin/python3

"""writing on a file"""


def write_file(filename="", text=""):
    """writing a string"""
    length = 0
    with open(filename, 'w', encoding="utf-8") as f:
        length = f.write(text)
    return (length)


if __name__ == "__main__":
    nb_chars = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_chars)
