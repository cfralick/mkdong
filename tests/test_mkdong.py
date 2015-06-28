try:
    import unittest2 as unittest
except ImportError:
    import unittest

import sys
from mkdong.mkdong import Dong
from argparse import ArgumentError

class DongTestCase(unittest.TestCase):

    def setUp(self):
        self.dong = Dong

    def tearDown(self):
        self.dong = None

    def test_dong_is_dong(self):
        self.assertTrue(True)
