import constants as const


def exit_atm():
    exit()


def deposit_money_to_atm(deposit: float, account: float) -> float:
    account += deposit
    return account


def get_money_from_atm(money: float, account: float) -> float:
    percent: float = count_withdraw_atm(money)
    account = account - money - percent
    return account


def count_withdraw_atm(summ: float) -> float:
    percent: float = summ * const.WITHDRAW
    if percent < const.WITHDRAW_MIN:
        percent = const.WITHDRAW_MIN
    elif percent > const.WITHDRAW_MAX:
        percent = const.WITHDRAW_MAX
    return percent


def is_rich(account: float) -> float:
    if account > const.WEALTH_SUM:
        account = account - account * const.WEALTH_TAX
    return account


def count_percent(account: float) -> float:
    percent: float = 1 + const.PERCENTAGE
    account *= percent
    return account
