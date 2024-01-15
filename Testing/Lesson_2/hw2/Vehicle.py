from abc import ABCMeta, abstractmethod


class Vehicle():
    __metaclass__ = ABCMeta
    company: str
    model: str
    year_release: int
    num_wheels: int
    speed: int

    @abstractmethod
    def test_drive(self):
        pass

    @abstractmethod
    def park(self):
        pass
