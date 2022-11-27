#!/usr/bin/python3
"""file storage class
"""

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
        new_value = obj.to_dict()
        self.__objects[new_name] = new_value

    def save(self):
        """serialize __objects into JSON file
        """
        new_dict = {}
        for key in self.__objects.keys():
            new_dict[key] = self.__objects[key]
        with open(self.__file_path, mode="w") as to_file:
            json.dump(new_dict, to_file)
        """if not os.path.exists(self.__file_path):
            with open(self.__file_path, 'w') as file:
                temp = {}
                for key, obj in self.__objects.items():
                    temp.update({key: obj})
                file.write(json.dumps(temp))
        else:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
            data.update(self.__objects.items())
            with open(self.__file_path, 'w') as file:
                json.dump(data, file)"""

    def reload(self):
        """deserialize JSON file into __objects
        """
        if not os.path.exists(self.__file_path):
            pass
        else:
            with open(self.__file_path, 'r') as file:
                temp = json.load(file)
            self.__objects = temp
