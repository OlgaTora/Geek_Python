# Для создания самого файла csv с базой
# with open('logger.csv', 'w') as file:
#     pass


def logger_in_file(data: float):
    with open('logger_ATM.txt', 'a') as file:
        file.write(f'{data}\n')


def logger_in_list(data: float, list_for_operations: list[float]):
    list_for_operations.append(data)
    print(list_for_operations)


def create_list() -> list[float]:
    new_list = []
    return new_list

