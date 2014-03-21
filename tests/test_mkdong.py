import unittest
from mkdong.mkdong import mkdong, MAXLEN


class MkdongTestCase(unittest.TestCase):

    def setUp(self):
        self.default_dong = mkdong(1)
        self.maxlen = MAXLEN
        self.dong_too_long = MAXLEN + 1
    
    def tearDown(self):
        self.default_dong = None
        self.maxlen = 0
        self.dong_too_long = None

    def test_dong_is_dong(self):
        dong = '( )/( )/D'
        self.assertEqual(mkdong(1), dong)
    
    def test_microdong_is_still_dong(self):
        micro = '( )/( )D'
        self.assertEqual(mkdong(0), micro)

    def test_default_dong_is_dong(self):
        self.assertEqual(mkdong(1), self.default_dong)
    
    def test_climaxing_dong_shows_load(self):
        self.assertEqual(mkdong(1, True), self.default_dong + '~~~~')

    @unittest.expectedFailure
    def test_max_dong_length_is_MAXLEN(self):
        self.assertTrue(mkdong(self.maxlen))
        self.assertTrue(mkdong(self.dong_too_long))

    def test_dong_too_long_raises_value_error(self):
        with self.assertRaises(ValueError):
            mkdong(self.dong_too_long)

    def test_unspecified_dong_length_raises_type_error(self):
        with self.assertRaises(TypeError):
            mkdong()

    def test_non_int_dong_length_raises_type_error(self):
        with self.assertRaises(TypeError):
            mkdong('penis')
    
    def test_superfluous_int_argument_raises_type_error(self):
        with self.assertRaises(TypeError):
            mkdong(10, None, 20)

    def test_superfluous_str_argument_raises_type_error(self):
        with self.assertRaises(TypeError):
            mkdong(10, None, 'cock')


