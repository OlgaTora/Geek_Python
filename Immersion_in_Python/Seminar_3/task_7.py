# Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается  каждая буква в строке без использования
# метода count и с ним.  Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи  символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают  или не совпадают в ваших решениях.


#data = input('Input something')
data = 'fhgjff djfk afdjka sdgjkdff'
dict_1 = {}
dict_2 = {}

for letter in set(data.replace(' ', '')):
    dict_1[letter] = data.count(letter)
print(dict_1)


for letter in data.replace(' ', ''):
    dict_2.setdefault(letter, 0)
    dict_2[letter] += 1
print(dict_2)

