from Testing.Lesson_2.hw2.Vehicle import Vehicle


class Motorcycle(Vehicle):

    def __init__(self, company: str, model: str, year: int):
        super().__init__()
        self.company = company
        self.model = model
        self.year_release = year
        self.num_wheels = 2
        self.speed = 0

    def test_drive(self):
        self.speed = 75

    def park(self):
        self.speed = 0

    def get_company(self) -> str:
        return self.company

    def get_model(self) -> str:
        return self.model

    def get_year_release(self) -> int:
        return self.year_release

    def get_num_wheels(self) -> int:
        return self.num_wheels

    def get_speed(self) -> int:
        return self.speed

    def __str__(self) -> str:
        return f'This motorcycle is a {self.year_release} year, model {self.model}'
