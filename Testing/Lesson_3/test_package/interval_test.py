import unittest
from parameterized import parameterized

from Testing.Lesson_3.hw3.interval import number_in_interval


class TestNumberInInterval(unittest.TestCase):

    @parameterized.expand([('test_1', 25, True), ('test_2', 100, True), ('test_3', 33, True), ('test_4', 99, True)])
    def test_number_in_interval(self, test_name, in_1, expected):
        """Check true if number in interval"""
        assert number_in_interval(in_1) == expected

    @parameterized.expand([('test_1', 24, False), ('test_2', 101, False), ('test_3', -25, False), ('test_4', 0, False)])
    def test_number_not_in_interval(self, test_name, in_1, expected):
        """Check false if number in interval"""
        assert number_in_interval(in_1) == expected
