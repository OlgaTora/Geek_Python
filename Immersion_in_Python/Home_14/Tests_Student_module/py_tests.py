import pytest
from Immersion_in_Python.Home_12.Student import Student

@pytest.fixture
def new_student():
    student1 = Student('Misha', 'Ivanovich', 'Krysha')
    return student1


@pytest.fixture
def list_of_progress():
    list_of_prog = {'Algebra': {'grades': [], 'test_results': []},
                    'Biology': {'grades': [], 'test_results': []},
                    'Drawing': {'grades': [], 'test_results': []},
                    'Chemistry': {'grades': [], 'test_results': []},
                    'Geography': {'grades': [], 'test_results': []},
                    'Geometry': {'grades': [], 'test_results': []},
                    'History': {'grades': [], 'test_results': []},
                    'Literature': {'grades': [], 'test_results': []}}
    return list_of_prog


@pytest.fixture
def list_of_progress_filled():
    list_of_progress_fill = {'Algebra': {'grades': [], 'test_results': []},
                             'Biology': {'grades': [], 'test_results': []},
                             'Drawing': {'grades': [5], 'test_results': []},
                             'Chemistry': {'grades': [3], 'test_results': []},
                             'Geography': {'grades': [3], 'test_results': [100]},
                             'Geometry': {'grades': [5], 'test_results': []},
                             'History': {'grades': [], 'test_results': [100, 50, 30]},
                             'Literature': {'grades': [], 'test_results': []}}
    return list_of_progress_fill


@pytest.fixture
def subject():
    subject = 'History'
    return subject


def test_append_grade_error(new_student, subject):
    with pytest.raises(ValueError):
        new_student.append_grade(1, subject)


def test_avg_tests(new_student, list_of_progress_filled, subject):
    new_student.list_of_progress = list_of_progress_filled
    assert f'Average result of tests of {new_student.__str__()} is: 60.0' == new_student.get_avg_test_result(subject)


if __name__ == '__main__':
    pytest.main(['-v'])
