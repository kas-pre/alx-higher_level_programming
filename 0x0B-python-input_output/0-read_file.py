#!/usr/bin/python3
"""Function reads text file(UTF-8)"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
