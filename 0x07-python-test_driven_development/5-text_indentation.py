#!/usr/bin/python3

"""
module import the function that  prints a text with
2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines after
    each of these characters: ., ? and :

    Args: text

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiter_set = {".", "?", ":"}
    current = ""
    for i, char in enumerate(text):
        if char in delimiter_set:
            if current:
                print(current.strip() + char, end="\n\n")
                current = ""
        else:
            current += char
    if current:
        print(current.strip(), end="")
