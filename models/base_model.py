#!/usr/bin/python3
"""defines all common attributes for all other classes
"""
import datetime
import uuid
from models import storage


class BaseModel():
    """all common methods/attributes
    """
    def __init__(self, *args, **kwargs):
        """create id, creation and update times
        can be created with dictionary(kwargs)
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    self.__dict__.update({'created_at':
                                         datetime.datetime.
                                         fromisoformat(value)})
                elif key == 'updated_at':
                    self.__dict__.update({'updated_at':
                                         datetime.datetime.
                                         fromisoformat(value)})
                else:
                    self.__dict__.update({key: value})
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """print name, id and __dict__attributes

        Returns:
            _str_: _description of current instance_
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update updated at time"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary of instance attributes

        Returns:
            _dict_: _key/values of instance attributes_
        """
        dictionary = {}
        dictionary.update({'__class__': self.__class__.__name__})
        dictionary.update(self.__dict__)
        dictionary.update({'created_at': self.created_at.isoformat(),
                          'updated_at': self.updated_at.isoformat()})
        return dictionary
