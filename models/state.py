#!/usr/bin/python3
"""DefinesState Class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Representstate subclass that inherits from the Basemodel.
    Attributes:
        name (str) Name . of the State
    """

    name = ""
