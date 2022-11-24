#!/usr/bin/python3
'''serializes instances to a JSON and 
deserializes JSON file to instances'''

import json
import os
class FileStorage():

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        new_name = f"{obj.__class__.__name__}.{obj.id}"
        new_value = obj.to_dict()
        self.__objects[new_name] = new_value

    def save(self):
        if not os.path.exists(self.__file_path):
            with open(self.__file_path, 'w') as file:
                temp = {}
                for key, obj in self.__objects.items():
                    temp.update({key: obj})
                file.write(json.dumps(temp))
        else:
            with open(self.__file_path, 'r') as file:
            #temp = {}
            #for key, obj in self.__objects.items():
            #    temp.update({key: obj})
            #file.write(json.dumps(temp))
                data = json.load(file)
            data.update(self.__objects.items())
            with open(self.__file_path, 'w') as file:
                json.dump(data, file)

    def reload(self):
        if not os.path.exists(self.__file_path):
            pass
        else:
            with open(self.__file_path, 'r') as file:
                temp = json.load(file)
            self.__objects = temp