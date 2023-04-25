#!/usr/bin/python3
"""Function serializes Python object"""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure"""
    return obj.__dict__
