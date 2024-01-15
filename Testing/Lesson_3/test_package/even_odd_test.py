import unittest

from Testing.Lesson_3.hw3.even_odd import even_odd_number


class TestEvenOdd(unittest.TestCase):

    def test_number_is_odd(self):
        self.assertEqual(even_odd_number(2), True)

    def test_number_is_even(self):
        self.assertEqual(even_odd_number(3), False)
