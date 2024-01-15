"""
Проект Vehicle. Написать следующие тесты с использованием Unit:
"""
import unittest

from Testing.Lesson_2.hw2.Motorcycle import Motorcycle


class TestMoto(unittest.TestCase):

    def setUp(self):
        self.moto = Motorcycle('buell', 'lighting', 2003)

    def tearDown(self):
        self.moto = None

    def test_count_wheels_moto(self):
        """Проверить, что объект Motorcycle создается с 2 - мя колесами."""
        self.assertEqual(self.moto.num_wheels, 2, msg='объект Motorcycle создается не с 2-мя колесами')

    def test_moto_speed_after_test_drive(self):
        """
        Проверить, что объект Motorcycle развивает скорость 75 в
        режиме тестового вождения (используя метод testDrive()).
        """
        self.moto.test_drive()
        self.assertTrue(75 == self.moto.speed, 'Motorcycle не развивает скорость 75 в режиме тестового вождения')

    def test_moto_speed_after_park(self):
        """
        Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта)
        мотоцикл останавливается (speed = 0).
        """
        self.moto.test_drive()
        self.moto.park()
        self.assertTrue(0 == self.moto.speed, 'Motorcycle не останавливается в режиме парковки')
