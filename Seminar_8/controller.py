import pandas as pd
import user_int as ui


def button():
    print('Велкам в базу данных, юзер!')
    ui.choice_action()


def get_data_txt(file):
    file = open(file)
    file = file.read()
    print(file)


def get_data_csv(file):
    df = pd.read_csv(file)
    return print(df)


def search_data_csv(file):
    df = pd.read_csv(file)
    smb_data = ui.get_smb_data()
    if (df['Surname'].eq(smb_data)).any():
        fnd = df.loc[df['Surname'] == smb_data]
        print(fnd)
    else:
        print('Нема такого персонажа, юзер')


def del_data_csv(file):
    df = pd.read_csv(file)
    smb_data = ui.get_smb_data()
    if (df['Surname'].eq(smb_data)).any():
        df = df.loc[df['Surname'] != smb_data]
        df.to_csv('logger.csv', index=False)
        print(df)
    else:
        print('Нельзя удалить то, чего нет, юзер')

