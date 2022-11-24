#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print('\n\n\n')
print(type(my_model.created_at))
print("--")
print('\n\n\n')
my_model_json = my_model.to_dict()
print(my_model_json)
print('\n'*2)
for key in my_model_json.keys():
    print("\t{}:    ({})    -   {}".format(key, type(my_model_json[key]), my_model_json[key]))
print("--")
my_new_model = BaseModel(**my_model_json)
print('\n'*2)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print("\n"*2)
print(my_model is my_new_model)