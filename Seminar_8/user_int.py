import controller as cc
import logger as log


def input_data():
    row = ''
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    tel = input('Введите номер телефона: ')
    info = input('Введите доп инфо: ')
    row = row + name + ',' + surname + ',' + tel + ',' + info
    return row


def get_smb_data():
    smb_data = input('Введите фамилию персонажа: ')
    return smb_data


def choice_action():
    try:
       try:
        print('Меню:', '\n',
                'Нажмите 1 - для работы с csv', '\n',
                'Нажмите 2 - для работы с txt')
        answer = int(input())
        if answer == 1:
            print('Меню: ', '\n',
                  '1 - Вывести все данные', '\n',
                  '2 - Вывести номер по фамилии', '\n',
                  '3 - Завести нового человека в базу', '\n',
                  '4 - Удалить человека из базы')
            answer = int(input())
            if answer == 1:
                cc.get_data_csv('logger.csv')
            elif answer == 2:
                cc.search_data_csv('logger.csv')
            elif answer == 3:
                lst = input_data()
                log.log_data_csv(lst)
            elif answer == 4:
                cc.del_data_csv('logger.csv')
        elif answer == 2:
            print('Меню: ', '\n',
                  '1 - Вывести все данные', '\n',
                  '2 - Завести нового человека в базу')
            answer = int(input())
            if answer == 1:
                cc.get_data_txt('logger.txt')
            elif answer == 2:
                lst = input_data()
                log.log_data_txt(lst)
       except:
        print('Вы можете выбрать csv или txt. Перезапустите')
    except:
        print('Ошибка')

