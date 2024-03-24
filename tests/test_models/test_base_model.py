#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
"""
Defines unittest module Basemodel class.
"""


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
