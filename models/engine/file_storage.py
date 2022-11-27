#!/usr/bin/python3
"""file storage class
"""
import datetime
import json
import os


class FileStorage():
    """this is a class that stores data by (de)serializing JSON
    """

    def __init__(self):
        """initiate path and dictionary
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """return dict of instance attributes

        Returns:
            _dict_: _stored instances_
        """
        return self.__objects

    def on_deletion(self, dictionary):
        """updates the dictionary on deletion

        Args:
            dictionay (_dict_): _dictionary with the removed instance_
        """
        self.__objects = dictionary.copy()

    def new(self, obj):
        """naming convention for every new instance

        Args:
            obj (_object_): _instance of a class_
        """
        new_name = f"{obj.__class__.__name__}.{obj.id}"
        new_value = obj
        self.__objects[new_name] = new_value

    def save(self):
        """serialize __objects into JSON file
        """
        with open(self.__file_path, 'w') as file:
            temp = {k: v.to_dict() for k, v in self.__objects.items()}
            file.write(json.dumps(temp))

    def reload(self):
        """deserialize JSON file into __objects
        """
        if not os.path.exists(self.__file_path):
            pass
        else:
            with open(self.__file_path, 'r') as file:
                loaded = json.load(file)
            from models.amenity import Amenity
            from models.base_model import BaseModel
            from models.city import City
            from models.review import Review
            from models.place import Place
            from models.state import State
            from models.user import User

            classes = {
                "Amenity": Amenity,
                "BaseModel": BaseModel,
                "City": City,
                "Review": Review,
                "Place": Place,
                "State": State,
                "User": User
            }
            temp = {}
            for k, v in loaded.items():
                j = k.split('.')[0]
                if j in classes.keys():
                    temp[k] = classes[j](**v)
            self.__objects.update(temp)
