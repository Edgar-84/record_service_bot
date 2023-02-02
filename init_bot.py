from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

from data.config import data

storage = MemoryStorage

bot = Bot(token=data.BOT_TOKEN)
dp = Dispatcher(bot, storage=storage())
