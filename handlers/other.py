from aiogram import types, Dispatcher
from init_bot import dp, bot


async def command_start(message: types.Message):
    await message.reply(f'Hi! Your id -> {message.from_user.id}')


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])