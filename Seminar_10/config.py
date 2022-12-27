from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils import get_data

BOT_KEY = get_data('../Torres_bot/key_bot.txt')


bot = Bot(token=BOT_KEY)
dp = Dispatcher(bot, storage=MemoryStorage())

