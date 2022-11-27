#!/usr/bin/python3
"""inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class for place accomodation is located

    Args:
        BaseModel (_BaseModel_): _inherit from base model_
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ''

    def __init__(self, *args, **kwargs):
        """create new place
        """
        super().__init__(self, *args, **kwargs)
