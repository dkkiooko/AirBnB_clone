#!/usr/bin/python3
"""test BaseModel class
"""
import datetime
import json
import pathmgc
import unittest
from models import base_model


class TestBaseModelDocs(unittest.TestCase):
    """test BaseModel class for documentation

    Args:
        unittest (_unittest_): _module to set up tests for various scenarios_
    """
    @classmethod
    def setUpClass(cls) -> None:
        print("\n\n...TESTING DOCUMENTATION...\n")
        print('... for BaseModel class ...\n\n')

    def test_doc_file(self):
        """test whether module is documented
        """
        doc = base_model.__doc__
        self.assertIsNotNone(doc)

    def test_doc_class(self):
        """test whether class is documented
        """
        doc = base_model.BaseModel.__doc__
        self.assertIsNotNone(doc)

    def test_doc_init(self):
        """test whether init function is documented
        """
        doc = base_model.BaseModel.__init__.__doc__
        self.assertIsNotNone(doc)

    def test_doc_save(self):
        """test whether save function is documented
        """
        doc = base_model.BaseModel.save.__doc__
        self.assertIsNotNone(doc)

    def test_doc_to_dict(self):
        """test whether to_dict function is documented
        """
        doc = base_model.BaseModel.to_dict.__doc__
        self.assertIsNotNone(doc)

    def test_doc_str(self):
        """test whether str function is documented
        """
        doc = base_model.BaseModel.__str__.__doc__
        self.assertIsNotNone(doc)


class TestBaseModelInstances(unittest.TestCase):
    """test whether instances of BaseModel work as expected

    Args:
        unittest (_unittest_): _class that helps us test modules_
    """
    @classmethod
    def setUpClass(cls):
        """initialize instance for testing
        """
        print('\n\n....TESTING FUNCTIONS...\n')
        print('... for BaseModel class ...\n')

    def setUp(self):
        """initialize BaseModel instance
        """
        self.obj = base_model.BaseModel()

    def test_str(self):
        """test whether __str__ function works
        """
        my_str = str(self.obj)
        my_list = ['BaseModel', 'id', 'created_at']
        total = 0
        for sub in my_list:
            if sub in my_str:
                total = total + 1
        self.assertTrue(3 == total)

    def test_updated(self):
        """test whether update time is being recorded
        """
        self.obj.save()
        time = self.obj.updated_at
        self.assertIsInstance(time, type(datetime.datetime.today()))

    def test_to_dict(self):
        """test whether to_dict returns serializable object
        """
        obj_dict = self.obj.to_dict()
        actual = 1
        try:
            serialized = json.dumps(obj_dict)
        except Exception:
            actual = 0
        self.assertTrue(1 == actual)

    def test_attribute(self):
        """test whether you can add attribute to object
        """
        self.obj.name = "Dan"
        self.assertEqual(self.obj.name, "Dan")


if __name__ == '__main__':
    unittest.main
