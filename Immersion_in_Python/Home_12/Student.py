"""
Создайте класс студента.
Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв.
Названия предметов должны загружаться из файла CSV при создании
экземпляра. Другие предметы в экземпляре недопустимы.
Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
тестов (от 0 до 100).
Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых.
"""
import csv
import json

from Descriptor import DescriptorName


class Student:
    file_name = 'list_of_subjects.csv'
    name = DescriptorName()
    patronymic = DescriptorName()
    surname = DescriptorName()
    max_grade = 5
    min_grade = 2
    max_test = 100
    min_test = 0

    def __init__(self, name: str, patronymic: str, surname: str):
        self.surname = surname
        self.patronymic = patronymic
        self.name = name
        self.list_of_subjects = self.read_csv(self.file_name)
        self.list_of_progress = self.create_list_progress()

    def __str__(self):
        return '_'.join([self.surname, self.name[0], self.patronymic[0]])

    def create_file_name(self) -> str:
        """Function for create file name with FIO of student"""
        file_name = self.__str__() + '.json'
        return file_name

    @staticmethod
    def read_csv(file_name) -> list:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = list(csv.DictReader(file, dialect='excel'))
            list_of_subjects = [''.join([subject for key, subject in i.items()]) for i in data]
            return list_of_subjects

    def create_list_progress(self) -> dict:
        """Function for get list of progress of student"""
        list_of_progress = {subject: {'grades': [], 'test_results': []} for subject in self.list_of_subjects}
        return list_of_progress

    def check_subject(self, subject: str):
        """Function for check learn this student this subject or not"""
        if subject not in self.list_of_subjects:
            raise ValueError('This subject is not learn by this student')

    def append_test(self, test_result: int, subject: str):
        """Function for append test results and check value"""
        self.check_subject(subject)
        if test_result > self.max_test or test_result < self.min_test:
            raise ValueError('Test result may be between 0 and 100')
        else:
            self.list_of_progress[subject]['test_results'].append(test_result)

    def append_grade(self, grade: int, subject: str):
        """Function for append grades and check value """
        self.check_subject(subject)
        if grade > self.max_grade or grade < self.min_grade:
            raise ValueError('Test result may be between 2 and 5')
        else:
            self.list_of_progress[subject]['grades'].append(grade)

    def get_avg_test_result(self, subject: str):
        """Function for receive average result of tests of one subject"""
        self.check_subject(subject)
        list_of_test = [i for i in self.list_of_progress[subject]['test_results']]
        result = sum(list_of_test) / len(list_of_test)
        return f'Average result of tests of {self.__str__()} is: {result}'

    def get_avg_grades(self):
        """Function for receive average result of grades at all subjects"""
        list_of_grades = [i for j in self.list_of_progress.values() for i in j['grades']]
        result = sum(list_of_grades) / len(list_of_grades)
        return f'Average grade of {self.__str__()} is: {result}'

    def save2json(self) -> None:
        file_name = self.create_file_name()
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(self.list_of_progress, file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    st1 = Student('Misha', 'Ivanovich', 'Krysha')
    print(f'Student 1 - {st1}')
    # st2 = Student('Misha', 'ivanovich', 'Krysha')
    # st3 = Student('Misha', 'I2vanovich', 'Krysha5')
    print('____________________________')
    # tests
    st1.append_test(99, 'Biology')
    st1.append_test(50, 'Biology')
    # st1.append_test(150, 'Biology')
    # st1.append_test(50'Biologdy')
    print(st1.get_avg_test_result('Biology'))
    print('____________________________')
    # grades
    st1.append_grade(4, 'Drawing')
    st1.append_grade(3, 'Biology')
    print(st1.get_avg_grades())
    print('____________________________')
    # save to json
    st1.save2json()
