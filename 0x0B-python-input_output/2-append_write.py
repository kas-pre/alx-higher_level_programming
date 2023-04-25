#!/usr/bin/python3
"""Function appends string at end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """Appends a string to end of a UTF8 text file

    Args:
        filename (str): Name of file to append to
        text (str): String to append to the file
    Returns:
        num of chars appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
