#!/usr/bin/python3

"""appending a text"""


def append_write(filename="", text=""):
    """adding to a text"""
    with open(filename, mode='a', encoding="utf-8") as f:
        length = 0
        length = f.write(text)

        return (length)


if __name__ == "__main__":
    char_added = append_write("file_append.txt", "This School is so cool!\n")
    print(char_added)
