from aiogram import types, Dispatcher
from keyboards import get_ikb_menu_other, get_ikb_menu_client


clients_list = []


async def command_start(message: types.Message):
    user_id = message.from_user.id
    if user_id in clients_list:
        await message.answer(f'Меню клиента: {message.from_user.username}',
                             reply_markup=await get_ikb_menu_client())

    else:
        await message.answer(f'Здравствуйте {message.from_user.username}! Your id -> {user_id}',
                             reply_markup=await get_ikb_menu_other())

    await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
