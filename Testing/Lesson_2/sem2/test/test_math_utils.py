"""Напишите тесты с использованием ассертов
 assertEquals, assertTrue, assertFalse, assertNull, assertNotNull
  и проверьте работу методов на различных наборах данных.
"""
import unittest

from Testing.Lesson_2.sem2.math_utils import MathUtils


class TestMathUtils(unittest.TestCase):

    def setUp(self):
        self.mathutils = MathUtils()

    def tearDown(self):
        self.mathutils = None

    def test_add(self):
        self.assertEqual(self.mathutils.add(2, 3), 5)

    def test_subtract(self):
        self.assertTrue(5 == self.mathutils.subtract(12, 7))

    def test_multiply(self):
        self.assertFalse(15 != self.mathutils.multiply(3, 5))

    def test_is_not_null(self):
        self.assertIsNotNone(self.mathutils)
