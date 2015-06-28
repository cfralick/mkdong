# -*- coding: utf-8 -*-

"""
module tests.test_mkdong 

"""

try:
    import unittest2 as unittest
except ImportError:
    import unittest
import sys
import argparse
import mkdong
from mkdong.mkdong import Dong, DongTooLong
from argparse import ArgumentError, Namespace


class DongTestCase(unittest.TestCase):
    """This test suite is unfinished."""

    def setUp(self):
        self.dong = Dong
        self.default_dong = '( )/( )D'

    def tearDown(self):
        self.dong = None
        self.default_dong = None

    def test_dong_is_dong(self):
        args = Namespace(outfile=None, length=0, climax=0, width=0)
        self.assertIsInstance(Dong(args), Dong)

    def test_dong_has_head(self):
        self.assertEqual(Dong.HEAD, 'D')
    
    def test_dong_has_two_balls(self):
        self.assertTrue(True)
   
    def test_dong_is_thin_by_default(self):
        self.assertEqual('-', Dong.WIDTH[0])
    
    def test_dong_climaxes_when_told(self):
        self.assertTrue(True)

    def test_dong_cums_harder_when_told(self):
        self.assertTrue(True)

    def test_dong_cannot_be_teased(self):
        self.assertTrue(True)
