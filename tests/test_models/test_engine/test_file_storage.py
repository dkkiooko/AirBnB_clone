#!/usr/bin/python3
""" Unit test for file_storage.py
"""
import json
import pathmagic
import unittest
import models
from models.base_model import BaseModel


class TestFileStorageDocs(unittest.TestCase):
    """class for testing FileStorage docs

    Args:s
        unittest (_unittest_): _TestCase class to try diff secnarios_
    """
    @classmethod
    def setUpClass(cls):
        print('\n\n...TESTING DOCUMENTATION...\n')
        print('.....FileStorage.....\n')

    def test_doc_module(self):
        """test documentation for module
        """
        documentation = models.file_storage.__doc__
        self.assertIsNotNone(documentation)

    def test_doc_class(self):
        """test documentation for class
        """
        documentation = models.file_storage.FileStorage.__doc__
        self.assertIsNotNone(documentation)

    def test_doc_all(self):
        """test documentation for the all() function
        """
        documentation = models.file_storage.FileStorage.all.__doc__
        self.assertIsNotNone(documentation)

    def test_doc_new(self):
        """test documentation for the new() function
        """
        documentation = models.file_storage.FileStorage.new.__doc__
        self.assertIsNotNone(documentation)

    def test_doc_save(self):
        """test documentation for the save function
        """
        documentation = models.file_storage.FileStorage.save.__doc__
        self.assertIsNotNone(documentation)

    def test_doc_reload(self):
        """test documentation for the reload function
        """
        documentation = models.file_storage.FileStorage.reload.__doc__
        self.assertIsNotNone(documentation)


class TestFileStorageInstances(unittest.TestCase):
    """test

    Args:
        unittest (_unittest_): _Testcases to try different scenarios_
    """
    @classmethod
    def setUpClass(cls) -> None:
        print('\n\n...TESTING INSTANCES...')
        print('...FileStorage...\n......')

    def setUp(self):
        """initialize new objects for testing
        """
        self.storage = models.file_storage.FileStorage()
        self.obj = BaseModel()

    def test_instantiation(self):
        """check proper FileStorage instation
        """
        self.assertIsInstance(self.storage,
                              type(models.file_storage.FileStorage()))
        self.assertIsInstance(self.obj, type(BaseModel()))

    def test_all(self):
        """check if all() returns new instance
        """
        bm_id = f"BaseModel.{self.obj.id}"
        all_obj = models.storage.all()
        self.assertIn(bm_id, all_obj.keys())

    def test_to_json(self):
        """test whether to_dict returns serializable JSON Object
        """
        my_model_json = self.obj.to_dict()
        actual = 1
        try:
            json.dumps(my_model_json)
        except Exception:
            actual = 0
        self.assertTrue(1 == actual)

    def test_reload(self):
        """test the relaod function
        """
        self.obj.save()
        bm_id = f"BaseModel.{self.obj.id}"
        new_storage = models.file_storage.FileStorage()
        new_storage.reload()
        all_obj = new_storage.all()
        self.assertIn(bm_id, all_obj.keys())


if __name__ == '__main__':
    unittest.main
