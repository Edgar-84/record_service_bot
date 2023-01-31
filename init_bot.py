from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from data.config import data

bot = Bot(token=data.BOT_TOKEN)
dp = Dispatcher(bot)
