#!/usr/bin/python3
"""Defines the Reviews Class method."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representing a review.

    Attributes:
        place_id: (str) The Place id.
        user_id: (str): The user id.
        text: (str): Actual text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
