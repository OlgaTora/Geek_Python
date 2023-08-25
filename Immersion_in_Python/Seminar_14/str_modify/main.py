"""
Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
"""
from string import ascii_letters


def string_modify(text: str) -> str:
    # """
    # Function for modify string to lowcase leaving only english letters and space
    #
    # Tests
    # строка без изменений
    # >>> string_modify('it was long thought')
    # 'it was long thought'
    #
    # строка с изменением регистра
    # >>> string_modify('It was Long thought')
    # 'it was long thought'
    #
    # строка с удалением пунктуации
    # >>> string_modify('it was, long thought!')
    # 'it was long thought'
    #
    # строка с удалением букв другого алфавита
    # >>> string_modify('it was long thought да дорогая')
    # 'it was long thought  '
    #
    # строки со всеми пт, кроме 1
    # >>> string_modify('It was Long thought, да дорогая?')
    # 'it was long thought  '
    # """
    return (''.join(letter for letter in text if letter in ascii_letters or letter == ' ')).lower()


# print(string_modify('It was long thought that коты domestication began in ancient Египет в 3100 BCб but recent advances'
#                    '\in archaeology and genetics have shown that their domestication occurred around 7500 BC'))

if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
