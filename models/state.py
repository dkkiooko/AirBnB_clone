#!/usr/bin/python3
"""inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """class for state where accomodation is

    Args:
        BaseModel (_BaseModel_): _inherit from base model_
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """create new state
        """
        super().__init__(self, *args, **kwargs)
