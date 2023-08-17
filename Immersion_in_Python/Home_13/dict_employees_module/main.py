from dict_employee import create_dict_employees

if __name__ == '__main__':
    names = ['Ivanov', 'Petrov', 'Popov']
    salaries = [100000, 200000, 35000]
    percentages = ['11.5%', '15.2%', '2.15%']
    print(create_dict_employees(names, salaries, percentages))

    #salaries = [100000, 200000, 5000]
    #percentages = ['11.5%', '15.2%', '-2.15%']
    names = ['Ivanov', 'Petrov', 'Popov3']
    print(create_dict_employees(names, salaries, percentages))
