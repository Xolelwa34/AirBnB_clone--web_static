#!/usr/bin/python3
"""Defines State Class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Representstate subclass that inherits from the Basemodel.

    Attributes:
        name: (str) name of the State
    """

    name = ""
