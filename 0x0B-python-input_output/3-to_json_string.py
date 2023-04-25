#!/usr/bin/python3
"""Function returns JSON representation of obj(str)"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object"""
    return json.dump(my_obj)
