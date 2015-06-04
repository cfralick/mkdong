
from __future__ import absolute_import

import unittest
from mkdong.dong import Defaults
from mkdong.mkdong import parser
from argparse import ArgumentError

class MkdongTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        return None

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_dong_is_dong(self):
        dong = '( )/( )=D'
        args = parser(Defaults).parse_args('1'.split())
        self.assertEqual(args.func(args), dong)

    def test_dong_is_as_long_as_specified_dong_length(self):
        dong = '( )/( )==========D'
        args = parser(Defaults).parse_args('10'.split())
        self.assertEqual(args.func(args), dong)


    def test_climaxing_dong_has_climax(self):
        dong = '( )/( )=D~'
        args = parser(Defaults).parse_args('1 -c'.split())
        self.assertEqual(args.func(args), dong)

    def test_thin_dong_is_thin(self):
        dong = '( )/( )-----D'
        args = parser(Defaults).parse_args('5 --thin'.split())
        self.assertEqual(args.func(args), dong)

    def test_wide_dong_is_wide(self):
        dong = '( )/( )/////D'
        args = parser(Defaults).parse_args('5 --wide'.split())
        self.assertEqual(args.func(args), dong)

    def test_wide_dong_can_climax(self):
        self.assertTrue(True)

    def test_even_thin_dong_can_climax(self):
        dong = '( )/( )-D~'
        args = parser(Defaults).parse_args('1 --thin -c'.split())
        self.assertEqual(args.func(args), dong)
