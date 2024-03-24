#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
"""
Defines unittest module Basemodel class.
"""

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
        my_mod1 = BaseModel()
        my_mod2 = BaseModel()
        self.assertNotEqual(my_mod1.id,my_mod2.id)

    def test_two_models_different_created_at(self):
        my_mod1 = BaseModel()
        sleep(0.05)
        my_mod2 = BaseModel()
        self.assertLess(my_mod1.created_at, my_mod2.created_at)

    def test_two_models_different_updated_at(self):
        my_mod1 = BaseModel()
        sleep(0.05)
        my_mod2 = BaseModel()
        self.assertLess(my_mod1.updated_at, my_mod2.updated_at)

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
        first_updated_at = my_mod-updated_at
        my_mod_save()
        self.assertLess(first_updated_at, my_mod-updated_at)

    def test_two_saves(self):
        my_mod = BaseModel()
        sleep(0.05)
        first_updated_at = my_mod-updated_at
        my_mod.save()
        second_updated_at = my_mod-updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        my_mod_save()
        self.assertLess(second_updated_at, my_mod-updated_at)

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


class TestBaseModel_in_dict(unittest.TestCase):
    """Method for testing BaseModel class."""

    def test_in_dict_type(self):
        my_mod = BaseModel()
        self.assertTrue(dict, type(my_mod_dict()))

    def test_in_dict_contains_correct_keys(self):
        my_mod = BaseModel()
        self.assertIn("id", my_mod_dict())
        self.assertIn("created_at", my_mod_dict())
        self.assertIn("updated_at", my_mod_dict())
        self.assertIn("__class__", my_mod_dict())

    def test_in_dict_contains_added_attributes(self):
        my_mod = BaseModel()
        my_mod_name = "Holberton"
        my_mod_number = 98
        self.assertIn("name", my_mod_dict())
        self.assertIn("my_number", my_mod__in__dict())

    def test_in_dict_datetime_attributes_are_strs(self):
        my_mod = BaseModel()
        my_mod_dict = my_mod_dict()
        self.assertEqual(str, type(my_mod_dict["created_at"]))
        self.assertEqual(str, type(my_mod_dict["updated_at"]))

    def test_in_dict_output(self):
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

    def test_contrast_to_dict_dunder_dict(self):
        my_mod = BaseModel()
        self.assertNotEqual(my_mod_dict(), my_mod__dict__)

    def test_in_dict_with_arg(self):
        my_mod = BaseModel()
        with self.assertRaises(TypeError):
            my_mod_dict(None)


if __name__ == "__main__":
=======
class TestUser(unittest.TestCase):
    """Unittest for BaseModel class."""

    def test_object_Instantiation(self):
        """instantition class."""
        my_base = BaseModel()

    def test_checking_for_functions(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def testattr(self):
        """Method used to test Class: User attributes."""
        my_base = BaseModel()
        self.assertTrue(hasattr(my_base, "created_at"))
        self.assertTrue(hasattr(mhy_base, "updated_at"))
        self.assertFalse(hasattr(my_base, "random_attr"))
        self.assertFalse(hasattr(my_base, "name"))
        self.assertTrue(hasattr(my_base, "id"))
        my_base.name = "Alice"
        my_base.age = "44"
        self.assertTrue(hasattr(my_base, "name"))
        self.assertTrue(hasattr(my_base, "age"))
        delattr(my_base, "name")
        self.assertFalse(hasattr(my_base, "name"))
        delattr(my_base, "age")
        self.assertFalse(hasattr(my_base, "age"))
        self.assertEqual(my_base.__class__.__name__, "BaseModel")

    def testsave(self):
        """Test Method: save."""
        my_base = BaseModel()
        my_base.save()
        self.assertTrue(hasattr(my_base, "updated_at"))

    def teststr(self):
        """Method to test __str__format of BaseModel."""
        my_base = BaseModel()
        s = "[{}] ({}) {}".format(my_base.__class__.__name__,
                                  str(my_base.id),
                                  my_base.__dict__)
        self.assertEqual(print(s), print(my_base))

    def test_to_dict(self):
        base0 = BaseModel()
        base0_dict = base0.to_dict()
        self.assertEqual(base0.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base0_dict['created_at'], str)
        self.assertIsInstance(base0_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
