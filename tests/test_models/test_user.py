#!/usr/bin/python3
"""unit test for class Amenity
"""
import pathmgc
import unittest
from models import user


class TestAmenityDocs(unittest.TestCase):
    """test documentation for class User

    Args:
        unittest (_type_): _description_
    """
    @classmethod
    def setUpClass(cls):
        print('\n\n...TESTING DOCUMENTATION...\n')
        print('\n..... AMENITY CLASS...\n')

    def test_doc_file(self):
        """test documentation for module
        """
        doc = user.__doc__
        self.assertIsNotNone(doc)

    def test_doc_class(self):
        """test class for documentation
        """
        doc = user.User.__doc__
        self.assertIsNotNone(doc)

    def test_doc_init(self):
        """test init function for documentation
        """
        doc = user.User.__init__.__doc__
        self.assertIsNotNone(doc)


if __name__ == '__main__':
    unittest.main
