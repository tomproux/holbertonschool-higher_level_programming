#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer(self, name, value):
        if name is str:
            if value is not int:
                raise TypeError("<name> must be an integer")
            elif value <= 0:
                raise TypeError("<name> must be greater than 0")
