import decimal as d
from exceptions import SalaryValueException, PercentValueException, NameValueException

MROT = 13000


def create_dict_employees(names: list, salaries: list, percentages: list):
    """
    Function for generate dictionary name: premium.
    Input 3 lists: names: str, salaries: int, percentages: str+%
    """
    dct = {}
    for i in list(zip(names, salaries, percentages)):
        if i[1] <= MROT:
            raise SalaryValueException(i[1])
        premium = i[2][:-1]
        if float(premium) <= 0:
            raise PercentValueException(i[2])
        if i[0].isalpha:
            raise NameValueException(i[0])
        dct[i[0]] = i[1] * d.Decimal(premium) / 100
    return dct
