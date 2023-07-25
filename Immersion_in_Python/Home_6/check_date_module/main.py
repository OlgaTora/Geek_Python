from sys import argv

from check_date import is_real_date, get_data

if __name__ == '__main__':
    # date, month, year = get_data()
    # print(is_real_date(date, month, year))
    #запуск в терминале
    name, *param = argv
    print(is_real_date(*(int(i) for i in param[0].split('.'))))

