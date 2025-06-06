#!/usr/bin/python3
"""Implements a function to print a person's name."""


def say_my_name(first_name, last_name=""):
    """Print a full name.

    Args:
        first_name (str): The first name to be printed.
        last_name (str): The last name to be printed (default is empty).
    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
