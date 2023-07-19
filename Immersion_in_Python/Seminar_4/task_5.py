"""
Функция принимает на вход три списка одинаковой длины:
имена str,
ставка int,
премия str с указанием процентов вида «10.25%».
Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии.
"""
import decimal as d
names = ['Ivanov', 'Petrov', 'Popov']
salaries = [1000, 2000, 15000]
percentages = ['11.5%', '15.2%', '2.15%']


def get_prize_dict(names:list[str], salaries:list[int], percentages:list[str]) -> dict[str:d.Decimal]:
    lst = list(zip(names, salaries, percentages))
    prize_dict = {}
    for name, salary, percentage in lst:
        prize_dict[name] = salary * d.Decimal(percentage[:-1]) / 100
    return prize_dict

print(get_prize_dict(names, salaries, percentages))

