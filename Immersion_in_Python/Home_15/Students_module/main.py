import argparse
from Student import Student


def parse():
    parser = argparse.ArgumentParser(prog='new student',
                                     description='add new student to data base"')
    parser.add_argument('-n', '--name',
                        help='student name',
                        type=str,
                        required=True)
    parser.add_argument('-p', '--patronymic',
                        help='student patronymic',
                        type=str)
    parser.add_argument('-s', '--surname',
                        help='student surname',
                        type=str,
                        required=True)
    arguments = parser.parse_args()
    st1 = Student(arguments.name, arguments.patronymic, arguments.surname)

    # tests
    st1.get_avg_test_result('Biology')
    st1.append_test(99, 'Biology')
    st1.append_test(50, 'Biology')
    #st1.append_test(150, 'Biology')
    #st1.append_test(50, 'Biologdy')
    st1.get_avg_test_result('Biology')

    # grades
    st1.append_grade(4, 'Drawing')
    st1.append_grade(3, 'Biology')
    st1.get_avg_grades()


if __name__ == '__main__':
    parse()
