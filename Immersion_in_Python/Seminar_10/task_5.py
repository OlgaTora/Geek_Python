"""
Создайте три (или более) отдельных классов животных.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.

Задание №6
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
"""


class Animal:
    def __init__(self, name: str, weight: int, speed: int):
        self.speed = speed
        self.weight = weight
        self.name = name

    def get_unique(self):
        pass


class Bird(Animal):
    def __init__(self, name: str, flight_altitude: int, weight: int, beak_length: int, speed: int):
        super().__init__(name, weight, speed)
        self.beak_length = beak_length
        self.flight_altitude = flight_altitude
        self.name = name

    def get_unique(self):
        return self.flight_altitude


class Fish(Animal):
    def __init__(self, name: str, deep: int, weight: int, fin_length: int, speed: int):
        super().__init__(name, weight, speed)
        self.deep = deep
        self.fin_length = fin_length

    def get_unique(self):
        return self.fin_length


class Predator(Animal):
    def __init__(self, name: str, weight: int, jump_altitude: int, tail_length: int, speed: int):
        super().__init__(name, weight, speed)
        self.tail_length = tail_length
        self.jump_altitude = jump_altitude

    def get_unique(self):
        return self.tail_length


if __name__ == '__main__':
    fish = Fish('fish', 25, 10, 2, 3)
    bird = Bird('bird', 30, 5, 1, 12)
    predator = Predator('cat', 10, 11, 40, 15)
    animals = (fish, bird, predator)
    for animal in animals:
        print(animal.get_unique())
