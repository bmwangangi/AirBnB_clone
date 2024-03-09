#!/usr/bin/python3

"""creates a new class called user to inherit from BaseModel."""

from models.base_model import BaseModel


class User(BaseModel):
    """class that inherits from base model."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""