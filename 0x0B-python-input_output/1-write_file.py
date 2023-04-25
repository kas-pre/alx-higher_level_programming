#!/usr/bin/python3
"""Function writes string to text file(UTF8)"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file

    Args:
        filename (str): The name of the file to write
        text (str): The text to write to the file
    Returns:
        Number of chars written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
