""" Модуль для сравнения среднего значения двух списков"""


class MeanComparator:
    """
    Класс для сравнения среднего значения двух списков
    """

    def __init__(self, list_first: list[float], list_second: list[float]):
        self.list_first = list_first
        self.list_second = list_second

    @staticmethod
    def get_mean(any_list: list) -> float | None:
        """
        Рассчитывает среднее значение списка.
        """
        if len(any_list) == 0:
            raise ValueError('Список не должен быть пустым')
        summ: float = 0.0
        for i in any_list:
            if type(i) != int and type(i) != float:
                raise TypeError('Список должен состоять из цифр')
            summ += i
        mean = summ / len(any_list)
        return mean

    def compare_mean(self) -> str:
        """
        Сравнивает средние значения списков и выводит соответствующее сообщение.
        """
        mean_first: float = self.get_mean(self.list_first)
        mean_second: float = self.get_mean(self.list_second)
        if mean_first > mean_second:
            result = 'Первый список имеет большее среднее значение'
        elif mean_first < mean_second:
            result = 'Второй список имеет большее среднее значение'
        else:
            result = 'Средние значения равны'
        return result
