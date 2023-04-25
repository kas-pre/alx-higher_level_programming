#!/usr/bin/python3
"""Function writes an object to a text file"""
import json


def save_to_json(my_obj, filename):
    """Write an object to a text file using JSON representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
