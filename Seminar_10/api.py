from aiogram import executor
from config import dp
from bot import set_default_commands


async def on_startup(dp):
    await set_default_commands(dp)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

