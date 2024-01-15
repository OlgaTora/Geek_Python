"""
Проект Vehicle. Написать следующие тесты с использованием Unit:
"""
import unittest

from Testing.Lesson_2.hw2.Vehicle import Vehicle
from Testing.Lesson_2.hw2.Car import Car


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car('honda', 'civic EG', 1996)

    def tearDown(self):
        self.moto = None

    def test_car_is_vehicle_type(self):
        """
        Проверить, что экземпляр объекта Car также является экземпляром транспортного средства
        (используя оператор instanceof).
        """
        type_to_test = Vehicle
        self.assertTrue(isinstance(self.car, type_to_test),
                        msg=f'экземпляр объекта Car не является экземпляром {type_to_test}')

    def test_count_wheels_car(self):
        """Проверить, что объект Car создается с 4-мя колесами."""
        self.assertEqual(self.car.num_wheels, 4, msg='объект Car создается не с 4-мя колесами')

    def test_car_speed_after_test_drive(self):
        """
        Проверить, что объект Car развивает скорость 60 в режиме тестового вождения
        (используя метод testDrive())."""
        self.car.test_drive()
        self.assertTrue(60 == self.car.speed, 'Car не развивает скорость 60 в режиме тестового вождения')

    def test_car_speed_after_park(self):
        """
        Проверить, что в режиме парковки(сначала testDrive, потом park, т.е.эмуляция движения транспорта)
        машина останавливается(speed=0).
        """
        self.car.test_drive()
        self.car.park()
        self.assertTrue(0 == self.car.speed, 'Car не останавливается в режиме парковки')
