class DigitsValueException(Exception):

    def __init__(self, min_value, max_value, attempts):
        self.attempts = attempts
        self.max_value = max_value
        self.min_value = min_value

    def __str__(self):
        return (f'You have input minimum={self.min_value}'
                f' and maximum={self.max_value},'
                f' and attempts={self.attempts}'
                f' Use only digits, please')


class AttemptsException(Exception):
    def __init__(self, attempts: int):
        self.attempts = attempts

    def __str__(self):
        return (f'Attempts cant be less than 1.'
                f' But you have input {self.attempts}')
