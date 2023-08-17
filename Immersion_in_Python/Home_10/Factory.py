from Animal import Animal
from ClassNotFoundException import ClassNotFoundException


class Factory:
    """
    Класс-фабрика:
    Класс принимает тип животного из класса Animal и параметры для этого типа.
    Создает экземпляр на основе переданного типа и возвращает егоерните его.
    """
    def create_object(self, class_name: str, *args):
        new_object = self._get_class(class_name)
        return new_object(*args)

    @staticmethod
    def _get_class(class_name: str):
        subclasses_ = Animal.__subclasses__()
        classes: dict = {c.__name__: c for c in subclasses_}
        class_ = classes.get(class_name, None)
        if class_ is not None:
            return class_
        else:
            raise ClassNotFoundException(class_)


if __name__ == '__main__':
    factory = Factory()
    animal1 = factory.create_object("Fish", 'Dorry', 11, 2, 5, 3)
    print(type(animal1))
    print(animal1.get_unique())
    animal2 = factory.create_object("Predator", 'Cat - Fagot', 11, 2, 5, 3)
    print(type(animal2))
    print(animal2.get_unique())
