# -*- coding: utf-8 -*-

"""
module tests.test_mkdong 

"""

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from mkdong.mkdong import Dong, DongTooLong
from argparse import ArgumentError


class DongTestCase(unittest.TestCase):
    """This test suite is unfinished."""

    def setUp(self):
        self.dong = Dong
        self.default_dong = '( )/( )D'

    def tearDown(self):
        self.dong = None
        self.default_dong = None

    def test_dong_is_dong(self):
        self.assertEqual(Dong().__class__, Dong)

    def test_default_dong_is_dong(self):
        self.assertEqual(self.default_dong, self.default_dong)
    
    def test_dong_has_two_balls(self):
        self.assertTrue(True)
   
    def test_dong_is_thin_by_default(self):
        self.assertTrue(True)
    
    def test_dong_climaxes_when_told(self):
        self.assertTrue(True)

    def test_dong_cums_harder_when_told(self):
        self.assertTrue(True)

    def test_dong_cannot_be_teased(self):
        self.assertTrue(True)
