#!/usr/bin/python3
"""test file for base_model
"""
import unittest
from models.base_model import BaseModel
class TestBaseModel(unittest.TestCase):
    """test all our base_model methods

    Args:
        unittest (_unittest.Testcase_): _inherit from unittest_
    """
    def test_str(self):
        temp = BaseModel()
        temp.name = "Example"
        temp.number = 89
        self.assertTrue(print(temp))