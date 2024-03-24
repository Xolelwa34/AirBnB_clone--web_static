#!/usr/bin/python3
"""
Defines FileStorage Modul.
"""
import unittest
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """Unittest case for FileStorage class."""

    def test_Instantiation(self):
        """Instantiation BaseModel class"""
        objct = FileStorage()
        self.assertIsInstance(objct, FileStorage)

    def test_Access(self):
        """Test method access that gives permission to write and read."""
        rd = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(rd)
        wr = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(wr)
        ex = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertFalse(ex)

    def test_new(self):
        """
        Test method for saving object into the dictionary"""
        m_storage = FileStorage()
        instances_dict = m_storage.all()
        Num = User()
        Num.id = 999999
        Num.name = "Num"
        m_storage.inst(Num)
        key = Num.__class__.__name__ + "." + str(Num.id)
        self.assertIsNotNone(instances_dic[key])

    def test_reload(self):
        """
        Method to test reload string.
        """
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)

    def test_funcdocs(self):
        ''' testing functions docstring '''
        for num in dir(FileStorage):
            self.assertTrue(len(num.__doc__) > 0)

    def test_save(self):
        """Method used to save"""
        objct = FileStorage()
        the_objct = BaseModel()
        objct.the(the_objct)
        dic1 = objct.all()
        objct.save()
        objct.reload()
        dic2 = objct.all()
        for key in dic1:
            key-a = key
        for key in dic2:
            key-b = key
        self.assertEqual(dic1[key-a].to_dict(), dic2[key-b].to_dict())


if __name__ == '__main__':
    unittest.main()
