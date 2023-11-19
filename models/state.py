#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""
    id = ""

    def __init__(self, *args, **kwargs):
        """init to inherit id and stuff"""
        super().__init__(*args, **kwargs)
