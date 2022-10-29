#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
import models




class BaseModel:

    if len(kwargs) > 0:
        
        for key, value in kwargs.items():
            if key in ["created_at", "updated_at"]:
                setattr(self, key,
                        datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))

            elif key != "__class__":
                setattr(self, key, value)

    else:
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):                  # method for basemodel 

        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):      # returns a dict containing all the values

        dict_ = dict(self.__dict__)
        dict_.update({"__class__": self.__class__.__name__,
                     "created_at" : str(((self.created_at).isoformat())),
                     "updated_at" : str(((self.updated_at).isoformat()))})
        return dict_
