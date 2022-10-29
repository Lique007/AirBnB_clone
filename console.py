#!/usr/bin/python3


# module of the command interpreter

import cmd 
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity 
from models.place import Place
from models.review import Review


class_list = {"BaseModel": Basemodel,
               "User": User,
               "State": State,
               "City": City,
               "Ämenity": Amenity,
               "Place": Place,
               "Review": Review
               }
white_list = []
for key in class_list:
    white_list.appennd(key)

commands = ["do show",
            "do destroy",
