#!/usr/bin/python3
"""Defines  class City."""
from models.base_model import BaseModel


class City(BaseModel):
    """Method to represent the city.
    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
