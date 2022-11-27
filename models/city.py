#!/usr/bin/python3
"""inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """class for city where accomodation is

    Args:
        BaseModel (_BaseModel_): _inherit from base model_
    """
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """create new city
        """
        super().__init__(self, *args, **kwargs)
