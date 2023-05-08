import unittest

from parameterized import parameterized

from anagrams.anagram import make_anagrams

class TestMakeAnagrams(unittest.TestCase):
    @parameterized.expand([
        ('abcd efgh', 'dcba hgfe'),
        ('a1bcd efg!h', 'd1cba hgf!e'),
        ('fgj124jklsdl', 'lds124lkjjgf'),
        ('45670896533 092290012', '45670896533 092290012'),
        ('=-12hkdf;d-./::"', '=-12dfdk;h-./::"'),
        ('', ''),
        (' ', ' ')
    ])
    def test_anagram(self, input_param, expected_value):
        self.assertEqual(make_anagrams(input_param), expected_value)

    @parameterized.expand([
        (TypeError, 1),
        (TypeError, ['s', 'a']),
        (TypeError, {'santa', 'vhkdfl'})

    ])
    def test_not_string(self, error, input):
        with self.assertRaises(error):
            make_anagrams(input)

