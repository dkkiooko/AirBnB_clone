#!/usr/bin/python3
"""inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """class for user lookin for accomodation

    Args:
        BaseModel (_BaseModel_): _inherit from base model_
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """create new user
        """
        super().__init__(self, *args, **kwargs)
