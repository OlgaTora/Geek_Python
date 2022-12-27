from aiogram import types
from aiogram.dispatcher import FSMContext
from Seminar_10.logger import logger
from utils import UserInputRat, UserInputComp, is_valid_rational, to_rational, calc, is_valid_complex, to_complex, \
    check_complex_res
from config import dp, bot
from aiogram.dispatcher.filters import Command

OPERATIONS = '+-*/'


# Создание команд для бота как меню
async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Запустить бота'),
            types.BotCommand('help', 'Справка'),
            types.BotCommand('calc_rational', 'Калькулятор\n рациональных чисел'),
            types.BotCommand('calc_complex', 'Калькулятор\n комплексных чисел'),
        ]
    )


# Хэндлер на start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привествую тебя, юзер!\n'
                        'Для работы переходи в меню')


# Хэндлер на help
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer('/calc_rational\n/calc_complex\n/help\n/start')


# Хэндлер на rational
@dp.message_handler(Command('calc_rational'))
async def start_rational(message: types.Message):
    await message.answer('Введите первое число\n через дробь: ')
    await UserInputRat.first_rat_num.set()


@dp.message_handler(state=UserInputRat.first_rat_num)
async def first_rat_num(message: types.Message, state: FSMContext):
    if not is_valid_rational(message.text):
        await message.answer('Необходимо ввести число,\n'
                             'через дробь')
        return
    await state.update_data(first_num=message.text)
    await UserInputRat.next()
    await message.answer('Введите мат операцию\n символом +=*/')


@dp.message_handler(state=UserInputRat.symbol)
async def second_rat_num(message: types.Message, state: FSMContext):
    if message.text not in OPERATIONS:
        await message.answer('Я работаю только с +-*/ ')
        return
    await state.update_data(symb=message.text)
    await UserInputRat.next()
    await message.answer('Введите второе число\n через дробь: ')


@dp.message_handler(state=UserInputRat.second_rat_num)
async def operation_rational(message: types.Message, state: FSMContext):
    data = await state.get_data()
    symb = data['symb']
    first_num = to_rational(data['first_num'])
    if not is_valid_rational(message.text):
        await message.answer('Необходимо ввести число,\n'
                             'через дробь')
        return
    second_num = to_rational(message.text)
    res = calc(first_num, second_num, symb)
    log = f"{data['first_num']} {symb} {message.text} = {res}"
    logger(log)
    await message.answer(log)
    await state.finish()


# Хэндлер на complex
@dp.message_handler(Command('calc_complex'))
async def start_complex(message: types.Message):
    await message.answer('Введите первое комплексное число без пробелов: ')
    await UserInputComp.first_comp_num.set()


@dp.message_handler(state=UserInputComp.first_comp_num)
async def first_comp_num(message: types.Message, state: FSMContext):
    if not is_valid_complex(message.text):
        await message.answer('Необходимо ввести число,\n'
                             'комплексное!')
        return
    await state.update_data(first_num=message.text)
    await UserInputComp.next()
    await message.answer('Введите мат операцию \n символом +=*/')


@dp.message_handler(state=UserInputComp.symbol)
async def second_comp_num(message: types.Message, state: FSMContext):
    if message.text not in OPERATIONS:
        await message.answer('Я работаю только с +-*/ ')
        return
    await state.update_data(symb=message.text)
    await UserInputComp.next()
    await message.answer('Введите второе комплексное число без пробелов: ')


@dp.message_handler(state=UserInputComp.second_comp_num)
async def operation_complex(message: types.Message, state: FSMContext):
    data = await state.get_data()
    symb = data['symb']
    first_num = to_complex(data['first_num'])
    if not is_valid_complex(message.text):
        await message.answer('Необходимо ввести число,\n'
                             'комплексное!')
        return
    second_num = to_complex(message.text)
    res = calc(first_num, second_num, symb)
    res = check_complex_res(res)
    log = f"{data['first_num']} {symb} {message.text} = {res}"
    await message.answer(log)
    logger(log)
    await state.finish()


#  Сообщения в "нулевом" состоянии:
@dp.message_handler()
async def unknown_message(msg: types.Message):
    msg.text = 'Это калькулятор!\n А не то, что подумали!'
    await bot.send_message(msg.from_user.id, msg.text)


# Если вводить числа рациональные в одну строку
#     if s.count('/') == 3:
#         s1 = s[::s.find('/')] + s[s.find('/'):s.find('/')]
#         s2 = s[s.find('/') - 1::]
#         # s1 = to_rational(s1)
#         # s2 = to_rational(s2)
