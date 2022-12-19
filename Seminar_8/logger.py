import pandas as pd
# Для создания самого файла csv с базой
# with open('logger.csv', 'w') as file:
#     pass
# data = pd.DataFrame(columns=['Name', 'Surname', 'Tel', 'Info'])
# Чтобы сохранялось без индексов
# data.to_csv('logger.csv', index=False)

# Для создания самого файла txt
# with open('logger.txt', 'w') as file:
#     pass


def log_data_txt(row):
    lst = row.split(',')
    with open('logger.txt', 'a') as file:
        file.write(f'\nName: {lst[0]}\n'
                   f'Surname:  {lst[1]}\n'
                   f'Tel:  {lst[2]}\n'
                   f'Info: {lst[3]}\n')


def log_data_csv(row):
    with open('logger.csv', 'a') as file:
        file.write(row)

