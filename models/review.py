#!/usr/bin/python3

"""creates a class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """class inherits form BaseModel."""
    place_id = ""
    user_id = ""
    text = ""