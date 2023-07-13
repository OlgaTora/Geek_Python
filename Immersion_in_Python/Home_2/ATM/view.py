import controller as c
import constants as const

global account


def get_action() -> int:
    print('Welcome to AMT machine:\n')
    data: int = int(prompt('push 1 to exit\n'
                           'push 2 to get money\n'
                           'push 3 to deposit money\n'))
    return data


def exit_atm():
    print('You are leaving ATM machine now')
    c.exit_atm()


def deposit(account: float) -> float:
    money: float = int(input('Input how much money you want to deposit:\n'))
    if money % const.MULTIPLE_SUM != 0:
        print(f'You have to input sum multiple {const.MULTIPLE_SUM}')
    else:
        curr_account: float = c.deposit_money_to_atm(money, account)
        return curr_account


def get_money(account: float) -> float:
    money: float = int(input('Input how much money you want to get:\n'))
    if money % const.MULTIPLE_SUM != 0:
        print(f'You have to get sum multiple {const.MULTIPLE_SUM}')
    elif money > account:
        print('You cant get more money than have')
    else:
        curr_account: float = c.get_money_from_atm(money, account)
        return curr_account


def operations(account: float, counter: int) -> float:
    curr_account: float = account
    prompt: int = get_action()
    account = c.is_rich(account)
    if account != curr_account:
        print('You have to pay tax')
    if prompt == 1:
        exit_atm()
    elif prompt == 2:
        curr_account = get_money(account)
    elif prompt == 3:
        curr_account = deposit(account)
    if counter % 3 == 0:
        curr_account = c.count_percent(curr_account)
        print(f'You have receive percentage')
    print(f'Account:  {round(curr_account, 2)}')
    return curr_account


def prompt(data: str) -> float:
    input_data = float(input(data))
    return input_data
