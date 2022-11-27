#!/usr/bin/python3
"""inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class for amenities in accomodation

    Args:
        BaseModel (_BaseModel_): _inherit from base model_
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """create new amenity
        """
        super().__init__(self, *args, **kwargs)
