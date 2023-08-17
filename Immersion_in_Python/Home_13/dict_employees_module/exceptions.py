class SalaryValueException(Exception):
    def __init__(self, salary: int):
        self.salary = salary

    def __str__(self):
        return (f'Salary cannot be less than MROT.'
                f'This salary is {self.salary}')


class PercentValueException(Exception):
    def __init__(self, percent: str):
        self.percent = percent

    def __str__(self):
        return (f'Percent cannot be less than 0.'
                f'This percent is {self.percent}')


class NameValueException(Exception):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return (f'Name has to contain only letters.'
                f'This name is {self.name}')
