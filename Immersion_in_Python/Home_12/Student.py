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
from Descriptor import DescriptorName


class Student:
    file_name = 'list_of_subjects.csv'
    name = DescriptorName()
    patronymic = DescriptorName()
    surname = DescriptorName()

    def __init__(self, name: str, patronymic: str, surname: str):
        self.surname = surname
        self.patronymic = patronymic
        self.name = name
        self.list_of_subjects = self.read_csv(self.file_name)
        self.list_of_progress = self.create_list_progress()


    def __str__(self):
        return f'111'

    def create_file_name(self) -> str:
        file_name = '_'.join([self.surname, self.name[0], self.patronymic[0]]) + '.csv'
        return file_name

    def read_csv(self, file_name) -> list:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = list(csv.DictReader(file, dialect='excel'))
            list_of_subjects = [''.join([subject for key, subject in i.items()]) for i in data]
            return list_of_subjects

    def create_list_progress(self) -> dict:
        list_of_progress = {subject: {'grades': [], 'test_results': []} for subject in self.list_of_subjects}
        return list_of_progress

    def check_subject(self, subject: str):
        if subject not in self.list_of_subjects:
            raise ValueError('This subject is not learn by this student')

    def append_test(self, test_result: int, subject: str):
        self.check_subject(subject)
        if test_result > 100 or test_result < 0:
            raise ValueError('Test result may be between 0 and 100')
        else:
            self.list_of_progress[subject]['test_results'].append(test_result)

    def append_grade(self, grade: int, subject: str):
        self.check_subject(subject)
        if grade > 5 or grade < 2:
            raise ValueError('Test result may be between 2 and 5')
        else:
            self.list_of_progress[subject]['grades'].append(grade)

    def get_avg_test_result(self, subject: str):
        """Function for receive average result of tests of one subject"""
        self.check_subject(subject)
        list_of_test = [i for i in self.list_of_progress[subject]['test_results']]
        result = sum(list_of_test) / len(list_of_test)
        return f'Average result of test is: {result}'

    def get_avg_grades(self):
        """Function for receive average result of grades at all subjects"""
        list_of_grades = [i for i in self.list_of_progress]
        print(list_of_grades)
       # result = sum(list_of_grades) / len(list_of_grades)
        #return f'Average result of grades is: {result}'

if __name__ == '__main__':
    st1 = Student('Misha', 'Ivanovich', 'Krysha')
    # st2 = Student('Misha', 'ivanovich', 'Krysha')
    # st3 = Student('Misha', 'I2vanovich', 'Krysha5')
    st1.append_test(99, 'Biology')
    print(st1.get_avg_test_result('Biology'))
    st1.append_grade(4, 'Drawing')
    print(st1.get_avg_grades())
