# -*- coding: utf-8 -*-

"""
module tests.test_mkdong

"""

try:
    import unittest2 as unittest
except ImportError:
    import unittest
import argparse
import mkdong
from mkdong.dong import DongParser, mkdong


class MkDongTestCase(unittest.TestCase):

    """This test suite is unfinished."""

    def setUp(self):
        self.dong = DongParser
        self.default_dong = '( )/( )-D'

    def tearDown(self):
        self.dong = None
        self.default_dong = None

    def test_dongparser_is_dongparser(self):
        self.assertIsInstance(DongParser(), argparse.ArgumentParser)
