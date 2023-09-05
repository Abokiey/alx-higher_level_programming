#!/usr/bin/python3

def text_indentation(text):
    """indents texts after ",?:" characters"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace("?", "?\n\n")
    text = text.replace(".", ".\n\n")
    text = text.replace(":", ":\n\n")

    for i in text:
        text = text.replace(" \n", "\n")
        text = text.replace("\n ", "\n")

    text = text.strip(" ")
    print(text, end="")
