# ✔ В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.


PATH = 'cats.txt'
PUNCTUATION = ('.,!?,;:"(*&^%#@><_/=÷×+[]–')
FREQUENT_COUNT = 10


def get_data(file):
    with open(file, 'r') as file:
        data = file.read()
    return data


def get_data_prepare(data: str) -> list:
    for i in PUNCTUATION:
        data = data.replace(i, '')
    data_list = data.lower().split()
    return data_list


def create_dict(data_list: list) -> dict:
    data_dict = {}
    for elem in data_list:
        data_dict.setdefault(elem, 0)
        data_dict[elem] += 1
    return data_dict


def count_duplicates(data_dict: dict) -> list:
    result = []
    for i in range(FREQUENT_COUNT):
        max_key = max(data_dict, key=data_dict.get)
        result.append(f'{max_key} = {data_dict.get(max_key)}')
        data_dict.pop(max_key)
    return result

data = get_data(PATH)
data_prepare = get_data_prepare(data)
data_dict = create_dict(data_prepare)
result: str = '\n'.join(count_duplicates(data_dict))
print(f'More frequency words in text is:\n{result}')
