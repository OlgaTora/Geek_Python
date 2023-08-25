import unittest

from Immersion_in_Python.Home_12.Student import Student
from Immersion_in_Python.Home_12 import Descriptor


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.student1 = Student('Misha', 'Ivanovich', 'Krysha')
        cls.list_of_progress = {'Algebra': {'grades': [], 'test_results': []},
                                'Biology': {'grades': [], 'test_results': []},
                                'Drawing': {'grades': [], 'test_results': []},
                                'Chemistry': {'grades': [], 'test_results': []},
                                'Geography': {'grades': [], 'test_results': []},
                                'Geometry': {'grades': [], 'test_results': []},
                                'History': {'grades': [], 'test_results': []},
                                'Literature': {'grades': [], 'test_results': []}}
        cls.list_of_progress_filled = {'Algebra': {'grades': [], 'test_results': []},
                                       'Biology': {'grades': [], 'test_results': []},
                                       'Drawing': {'grades': [5], 'test_results': []},
                                       'Chemistry': {'grades': [3], 'test_results': []},
                                       'Geography': {'grades': [3], 'test_results': [100]},
                                       'Geometry': {'grades': [5], 'test_results': []},
                                       'History': {'grades': [], 'test_results': [100, 50, 30]},
                                       'Literature': {'grades': [], 'test_results': []}}

        cls.non_subject = 'Russian'
        cls.subject = 'History'

    def test_create_list_progress(self):
        self.assertEquals(self.list_of_progress, self.student1.create_list_progress())

    def test_check_subject(self):
        with self.assertRaises(ValueError) as e:
            self.student1.check_subject(self.non_subject)
            self.assertEqual(str(e.exception), 'This subject is not learn by this student')

    def test_append_test_error(self):
        with self.assertRaises(ValueError) as e:
            self.student1.append_test(115, self.subject)
            self.assertEqual(str(e.exception), 'Test result may be between 0 and 100')

    def test_avg_grades(self):
        self.student1.list_of_progress = self.list_of_progress_filled
        self.assertEquals(f'Average grade of {self.student1.__str__()} is: 4.0',
                          self.student1.get_avg_grades())
