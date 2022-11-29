#!/usr/bin/python3
"""test module for the console
"""
import mgc_pth
import unittest
import console
from console import HBNBCommand


class Testconsole(unittest.TestCase):
    """testing the console

    Args:
        unittest (_unittest_): _module that tests various scenarios_
    """

    @classmethod
    def setUpClass(cls):
        """set up instance for test
        """
        cls.cli = HBNBCommand()

    @classmethod
    def teardown(cls):
        """destroy instance after end of test
        """
        del cls.cli

    def test_docstrings(self):
        """check for docstrings
        """
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_default.__doc__)

    def test_empty(self):
        """test empty line input
        """


if __name__ == '__main__':
    unittest.main
