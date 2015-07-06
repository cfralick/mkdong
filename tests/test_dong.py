# -*- coding: utf-8 -*-

"""
module tests.test_dong

"""

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from mkdong.dong import Dong
from argparse import FileType, Namespace
import sys


class DongTestCase(unittest.TestCase):

    def setUp(self):
        self.namespace = Namespace(length=0, width=0, climax=0, outfile=sys.stdout, head='D', wad='~')
        self.dong = Dong(**vars(self.namespace))

    def tearDown(self):
        self.dong = None

    def test_dong_is_a_dong(self):
        self.assertIsInstance(Dong(), Dong)
