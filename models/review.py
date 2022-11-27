#!/usr/bin/python3
"""inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class for reviews for accomodation

    Args:
        BaseModel (_BaseModel_): _inherit from base model_
    """
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """create new review
        """
        super().__init__(self, *args, **kwargs)
