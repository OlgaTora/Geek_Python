""" Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег

Доп задание в ДЗ4:
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""


from Immersion_in_Python.Home_2.ATM.view import operations
import constants as const
import controller as c


account = const.START_SUM
counter: int = 0
operation_list: list[float] = []

while True:
    try:
        counter += 1
        account, money = operations(account, counter)
        c.logger(money, operation_list)
        print('------------------')
    except ValueError:
        print('You have to input only numbers')
    except TypeError:
        print('Please, try again')

