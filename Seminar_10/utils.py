from aiogram.dispatcher.filters.state import StatesGroup, State


class UserInputRat(StatesGroup):
    first_rat_num = State()
    symbol = State()
    second_rat_num = State()


class UserInputComp(StatesGroup):
    first_comp_num = State()
    symbol = State()
    second_comp_num = State()


def get_data(file):
    with open(file) as file:
        return file.read()