""" Напишите тесты с использованием аннотаций
@Test,
@Before,
@After,
@BeforeClass,
@AfterClass
 для проверки различных сценариев, включая правильные и неправильные адреса"""
import unittest

from Testing.Seminar_2.task2.email_validator import EmailValidator


class TestEmailValidator(unittest.TestCase):
    def setUp(self):
        self.email_validator = EmailValidator()

    def tearDown(self):
        self.email_validator = None

    def test_is_valid_email(self):
        self.assertTrue(self.email_validator.is_valid_email("123kofa-ioh@mm"))

    def test_is_not_valid_email(self):
        self.assertFalse(self.email_validator.is_valid_email("123kofa-ioh"))
