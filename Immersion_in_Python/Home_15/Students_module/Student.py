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
from logger import logger
from Descriptor import DescriptorName


class Student:
    file_name = ('/home/olgatorres/PycharmProjects/Geek_Python/'
                 'Immersion_in_Python/Home_15/Students_module/list_of_subjects.csv')
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
        log_msg = f'Added new student: {self.name} {self.patronymic} {self.surname}'
        logger.info(log_msg)

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
            log_msg = f'This subject {subject} is not learn by this student {self.__str__()}'
            logger.error(log_msg)
            raise ValueError('This subject is not learn by this student')

    def append_test(self, test_result: int, subject: str):
        """Function for append test results and check value"""
        self.check_subject(subject)
        if test_result > self.max_test or test_result < self.min_test:
            log_msg = f'Test result may be between 0 and 100, you have input {test_result}'
            logger.error(log_msg)
            raise ValueError('Test result may be between 0 and 100')
        else:
            self.list_of_progress[subject]['test_results'].append(test_result)
            log_msg = f'Test result={test_result} - subject {subject} - {self.__str__()}'
            logger.info(log_msg)

    def append_grade(self, grade: int, subject: str) -> None:
        """Function for append grades and check value """
        self.check_subject(subject)
        if grade > self.max_grade or grade < self.min_grade:
            log_msg = f'Grade may be between 2 and 5, you have input {grade}'
            logger.error(log_msg)
            raise ValueError('Grade may be between 2 and 5')
        else:
            self.list_of_progress[subject]['grades'].append(grade)
            log_msg = f'Grade={grade} - subject {subject} - {self.__str__()}'
            logger.info(log_msg)

    def get_avg_test_result(self, subject: str):
        """Function for receive average result of tests of one subject"""
        self.check_subject(subject)
        list_of_test = [i for i in self.list_of_progress[subject]['test_results']]
        try:
            result = sum(list_of_test) / len(list_of_test)
            log_msg = f'Average result of tests of {self.__str__()} is: {result}'
            logger.info(log_msg)
        except ZeroDivisionError as e:
            logger.error(f'{e}: List of tests of {self.__str__()} is empty')

    def get_avg_grades(self):
        """Function for receive average result of grades at all subjects"""
        list_of_grades = [i for j in self.list_of_progress.values() for i in j['grades']]
        try:
            result = sum(list_of_grades) / len(list_of_grades)
            log_msg = f'Average grade of {self.__str__()} is: {result}'
            logger.info(log_msg)
        except ZeroDivisionError as e:
            logger.error(f'{e}: List of tests of {self.__str__()} is empty')

    def save2json(self) -> None:
        file_name = self.create_file_name()
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(self.list_of_progress, file, ensure_ascii=False, indent=2)
