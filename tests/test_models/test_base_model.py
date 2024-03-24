#!/usr/bin/python3
"""Defines unittests for base models class
Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Tests the instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        my_modA = BaseModel()
        my_modB = BaseModel()
        self.assertNotEqual(my_modA.id,my_modB.id)

    def test_two_models_different_created_at(self):
        my_modA = BaseModel()
        sleep(0.05)
        my_modB = BaseModel()
        self.assertLess(my_modA.created_at, my_modB.created_at)

    def test_two_models_different_updated_at(self):
        my_modA = BaseModel()
        sleep(0.05)
        my_modB = BaseModel()
        self.assertLess(my_modA.updated_at, my_modB.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date_repr = repr(date)
        my_mod = BaseModel()
        my_mod.id = "123456"
        my_mod.created_at = my_mod.updated_at = date
        my_modstr = my_mod.__str__()
        self.assertIn("[BaseModel] (123456)", my_modstr)
        self.assertIn("'id': '123456'", my_modstr)
        self.assertIn("'created_at': " + date_repr, my_modstr)
        self.assertIn("'updated_at': " + date_repr, my_modstr)

    def test_args_unused(self):
        my_mod = BaseModel(None)
        self.assertNotIn(None, bmod__in_dict__.values())

    def test_instantiation_with_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        my_mod = BaseModel(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(my_mod.id, "345")
        self.assertEqual(my_mod.created_at, date)
        self.assertEqual(my_mod-updated_at, date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        my_mod = BaseModel("12", id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(my_mod.id, "345")
        self.assertEqual(my_mod.created_at, date)
        self.assertEqual(my_mod-updated_at, date)


class TestBaseModel_save(unittest.TestCase):
    """Method to save BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        bmod = BaseModel()
        sleep(0.05)
        first_updated_at = my_mod.updated_at
        my_mod_save()
        self.assertLess(first_updated_at, my_mod.updated_at)

    def test_two_saves(self):
        my_mod = BaseModel()
        sleep(0.05)
        first_updated_at = my_mod.updated_at
        my_mod.save()
        second_updated_at = my_mod.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        my_mod_save()
        self.assertLess(second_updated_at, my_mod.pdated_at)

    def test_save_with_arg(self):
        my_mod = BaseModel()
        with self.assertRaises(TypeError):
            my_mod_save(None)

    def test_save_updates_file(self):
        my_mod = BaseModel()
        my_mod_save()
        my_modid = "BaseModel." + my_mod.id
        with open("file.json", "r") as f:
            self.assertIn(my_mod, f.read())


class TestBaseModel_dict(unittest.TestCase):
    """Method for testing BaseModel class."""

    def test_dict_type(self):
        my_mod = BaseModel()
        self.assertTrue(dict, type(my_mod_dict()))

    def test_dict_contains_correct_keys(self):
        my_mod = BaseModel()
        self.assertIn("id", my_mod_dict())
        self.assertIn("created_at", my_mod_dict())
        self.assertIn("updated_at", my_mod_dict())
        self.assertIn("__class__", my_mod_dict())

    def test_dict_contains_added_attributes(self):
        my_mod = BaseModel()
        my_mod_name = "Holberton"
        my_mod_number = 98
        self.assertIn("name", my_mod_dict())
        self.assertIn("my_number", my_mod_dict())

    def test_dict_datetime_attributes_are_strs(self):
        my_mod = BaseModel()
        my_mod_dict = my_mod_dict()
        self.assertEqual(str, type(my_mod_dict["created_at"]))
        self.assertEqual(str, type(my_mod_dict["updated_at"]))

    def test_dict_output(self):
        date = datetime.today()
        my_mod = BaseModel()
        my_mod.id = "123456"
        my_mod.created_at = my_mod.updated_at = date
        t_dict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat()
        }
        self.assertDictEqual(bmod_dict(), t_dict)

    def test_contrast_dict_dunder_dict(self):
        my_mod = BaseModel()
        self.assertNotEqual(my_mod_dict(), my_mod__dict__)

    def test_dict_with_arg(self):
        my_mod = BaseModel()
        with self.assertRaises(TypeError):
            my_mod_dict(None)


if __name__ == "__main__":
    unittest.main()
