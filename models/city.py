#!/usr/bin/python3

"""creates a class."""

from models.base_model import BaseModel


class City(BaseModel):
    """class inherites from BaseModel."""
    state_id = ""
    name = ""