"""
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
"""


class FactioralGen:
    def __init__(self, *args):
        if len(args) == 2:
            self.step = 1
            self.start, self.stop = args
        elif len(args) == 1:
            self.stop = args[0]
            self.start = 1
            self.step = 1
        else:
            self.start, self.stop, self.step, *_ = args

    @staticmethod
    def calculate(number: int):
        """Function for calculate factorial"""
        mult: int = 1
        for i in range(2, number + 1):
            mult *= i
        return mult

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            result = self.calculate(self.start)
            self.start += self.step
            return result
        raise StopIteration


if __name__ == '__main__':
    fact_gen = FactioralGen(10)
    for i, elem in enumerate(fact_gen, start=1):
        print(i, elem)
