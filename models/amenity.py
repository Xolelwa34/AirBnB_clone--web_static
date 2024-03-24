#!/usr/bin/python3
"""Defins class Amenity."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class method to represent amenity.

    Attribute:

        name: (str) Subclass that inherits from the amenity.
    """

    name = ""
