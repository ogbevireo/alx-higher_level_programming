#!/usr/bin/python3
"""
    Write the Python class MagicClass that does exactly
    the same as the following Python bytecode:

    Raises:
        TypeError: radius must be a number

    Returns:
        _type_: (self.__radius**2) * math.pi,
    """
import math

"""Class: a class that stores the properties of a circumference"""


class MagicClass:

    """Class that stores the properties
    of a circumference"""

    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    """ Method that calculates the area of the circumference """

    def area(self):
        return (self.__radius**2) * math.pi

    """ Method that calculates the perimeter of a circumference """

    def circumference(self):
        return 2 * math.pi * self.__radius
