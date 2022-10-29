#!/usr/bin/python3
"""
A module that tests the BaseModel class
"""
import unittest
from time import sleep
import os
from datetime import datetime
from uuid import uuid4

import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    The test for models.base_model.BaseModel
    """

    def test_if_BaseModel_instance_has_id(self):
        """
        Checks that instance has an id assigned on initialization
        """
        basemod = BaseModel()
        self.assertTrue(hasattr(basemod, "id"))

    def test_str_representation(self):
        """
        Checks if the string representation is appropriate
        """
        basemod = BaseModel()
        self.assertEqual(str(basemod),
                         "[BaseModel] ({}) {}".format(basemod.id, basemod.__dict__))

    def test_ids_is_unique(self):
        """
        Checks if id is generated randomly and uniquely
        """
        basemod1 = BaseModel()
        basemod2 = BaseModel()
        self.assertNotEqual(basemod1.id, basemod2.id)

    def test_type_of_id_is_str(self):
        """
        Checks that id generated is a str object
        """
        basemod = BaseModel()
        self.assertTrue(type(basemod.id) is str)

    def test_created_at_is_datetime(self):
        """
        Checks that the attribute 'created_at' is a datetime object
        """
        basemod = BaseModel()
        self.assertTrue(type(basemod.created_at) is datetime)

    def test_updated_at_is_datetime(self):
        """
        Checks that the attribute 'updated_at' is a datetime object
        """
        basemod = BaseModel()
        self.assertTrue(type(basemod.updated_at) is datetime)

    def test_two_models_different_created_at(self):
        """
        Checks that the attribute 'created_at' of 2 models are different
        """
        basemod1 = BaseModel()
        sleep(0.02)
        basemod2 = BaseModel()
        sleep(0.02)
        self.assertLess(basemod1.created_at, basemod2.created_at)

    def test_args_unused(self):
        """
        Checks that the attribute 'args' is not used.
        """
        basemod = BaseModel(None)
        self.assertNotIn(None, basemod.__dict__.values())

    def test_that_created_at_equals_updated_at_initially(self):
        """
        Checks that create_at == updated_at at initialization
        """
        basemod = BaseModel()
        self.assertEqual(basemod.created_at, basemod.updated_at)

    def test_that_save_func_update_update_at_attr(self):
        """
        Checks that save() method updates the updated_at attribute
        """
        basemod = BaseModel()
        basemod.save()
        self.assertNotEqual(basemod.created_at, basemod.updated_at)
        self.assertGreater(basemod.updated_at.microsecond,
                           basemod.created_at.microsecond)

    def test_if_to_dict_returns_dict(self):
        """
        Checks if BaseModel.to_dict() returns a dict object
        """
        basemod = BaseModel()
        self.assertTrue(type(basemod.to_dict()) is dict)

    def test_if_to_dict_returns_class_dunder_method(self):
        """
        Checks if BaseModel.to_dict() contains __class__
        """
        basemod = BaseModel()
        self.assertTrue("__class__" in basemod.to_dict())

    def test_that_created_at_returned_by_to_dict_is_an_iso_string(self):
        """
        Checks that created_at is stored as a str obj in ISO format
        """
        basemod = BaseModel()
        self.assertEqual(basemod.to_dict()["created_at"], basemod.created_at.isoformat())

    def test_that_updated_at_returned_by_to_dict_is_an_iso_string(self):
        """
        Checks that updated_at is stored as a str obj in ISO format
        """
        basemod = BaseModel()
        self.assertEqual(basemod.to_dict()["updated_at"], basemod.updated_at.isoformat())

    def test_if_to_dict_returns_the_accurate_number_of_keys(self):
        """
        Checks that to_dict() returns the expected number of keys/values
        """
        basemod = BaseModel()
        partial_expectation = {k: v for k, v in basemod.__dict__.items()
                               if not k.startswith("_")}
        self.assertEqual(len(basemod.to_dict()), len(partial_expectation) + 1)

    def test_when_kwargs_passed_is_empty(self):
        """
        Checks that id, created_at and updated_at are automatically
        generated if they're not in kwargs
        """
        my_dict = {}
        basemod = BaseModel(**my_dict)
        self.assertTrue(type(basemod.id) is str)
        self.assertTrue(type(basemod.created_at) is datetime)
        self.assertTrue(type(basemod.updated_at) is datetime)

    def test_when_kwargs_passed_is_not_empty(self):
        """
        Checks that id, created_at and updated_at are created from kwargs
        """
        my_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat()}
        basemod = BaseModel(**my_dict)
        self.assertEqual(basemod.id, my_dict["id"])
        self.assertEqual(basemod.created_at,
                         datetime.strptime(my_dict["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(basemod.updated_at,
                         datetime.strptime(my_dict["updated_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))

    def test_when_args_and_kwargs_are_passed(self):
        """
        When args and kwargs are passed, BaseModel should ignore args
        """
        dt = datetime.now()
        dt_iso = dt.isoformat()
        basemod = BaseModel("1234", id="234", created_at=dt_iso, name="Getie")
        self.assertEqual(basemod.id, "234")
        self.assertEqual(basemod.created_at, dt)
        self.assertEqual(basemod.name, "Getie")

    def test_when_kwargs_passed_is_more_than_default(self):
        """
        Checks BaseModel does not break when kwargs contains more than the default attributes
        """
        my_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat(),
                   "name": "Firdaus"}
        basemod = BaseModel(**my_dict)
        self.assertTrue(hasattr(basemod, "name"))

    def test_new_method_not_called_when_dict_obj_is_passed_to_BaseModel(self):
        """
        Test that storage.new() is not called when a BaseModel obj is created from a dict object
        """
        my_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat(),
                   "name": "Firdaus"}
        basemod = BaseModel(**my_dict)
        self.assertTrue(basemod not in models.storage.all().values(),
                        "{}".format(models.storage.all().values()))
        del basemod

        basemod = BaseModel()
        self.assertTrue(basemod in models.storage.all().values())

    def test_that_save_method_updates_updated_at_attr(self):
        """
        Checks that save() method updates 'updated_at' attribute
        """
        basemod = BaseModel()
        sleep(0.02)
        temp_update = basemod.updated_at
        basemod.save()
        self.assertLess(temp_update, basemod.updated_at)

    def test_that_save_can_update_two_or_more_times(self):
        """
        Tests that the save method updates 'updated_at' two times
        """
        basemod = BaseModel()
        sleep(0.02)
        temp_update = basemod.updated_at
        basemod.save()
        sleep(0.02)
        temp1_update = basemod.updated_at
        self.assertLess(temp_update, temp1_update)
        sleep(0.01)
        basemod.save()
        self.assertLess(temp1_update, basemod.updated_at)

    def test_save_update_file(self):
        """
        Tests if file is updated when the 'save' is called
        """
        basemod = BaseModel()
        basemod.save()
        bid = "BaseModel.{}".format(basemod.id)
        with open("file.json", encoding="utf-8") as f:
            self.assertIn(bid, f.read())

    def test_that_to_dict_contains_correct_keys(self):
        """
        Checks whether to_dict() returns the expected key
        """
        b_dict = BaseModel().to_dict()
        attrs = ("id", "created_at", "updated_at", "__class__")
        for attr in attrs:
            self.assertIn(attr, b_dict)

    def test_to_dict_contains_added_attributes(self):
        """
        Checks that new attributes are also returned by to_dict()
        """
        basemod = BaseModel()
        attrs = ["id", "created_at", "updated_at", "__class__"]
        basemod.name = "Getie"
        basemod.email = "getiebalew00@gmail.com"
        attrs.extend(["name", "email"])
        for attr in attrs:
            self.assertIn(attr, basemod.to_dict())

    def test_to_dict_output(self):
        """
        Checks the output returned by to_dict()
        """
        basemod = BaseModel()
        dt = datetime.now()
        basemod.id = "34567"
        basemod.created_at = basemod.updated_at = dt
        test_dict = {
            'id': "34567",
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(test_dict, basemod.to_dict())

    def test_to_dict_with_args(self):
        """
        Checks that TypeError is returned when argument is passed to to_dict()
        """
        basemod = BaseModel()
        with self.assertRaises(TypeError):
            basemod.to_dict(None)

    def test_to_dict_not_dunder_dict(self):
        """Checks that to_dict() is a dict object not equal to __dict__"""
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)


if __name__ == "__main__":
    unittest.main()