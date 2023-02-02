from aiogram import types, Dispatcher
from keyboards import get_ikb_menu_other, get_ikb_menu_client
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


clients_list = {}
all_tokens = ['123', '111']


class FSMRegistrationUser(StatesGroup):
    name = State()
    token = State()


async def command_start(message: types.Message):
    user_id = message.from_user.id
    if user_id in clients_list:
        await message.answer(f'Меню клиента: {message.from_user.username}',
                             reply_markup=await get_ikb_menu_client())

    else:
        await message.answer(f'Здравствуйте {message.from_user.username}! Your id -> {user_id}',
                             reply_markup=await get_ikb_menu_other())
    await message.delete()


async def set_new_user(callback: types.CallbackQuery):
    await FSMRegistrationUser.name.set()
    await callback.message.answer(f'Введите ваше имя:')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMRegistrationUser.next()
    await message.reply('Введите ТОКЕН для регистрации:')


async def load_token(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['token'] = message.text

        clients_list[message.from_user.id] = {'name': data['name'], 'token': data['token']}
        if data['token'] in all_tokens:
            await message.answer(f'Регистрация завершена, {clients_list}',
                                 reply_markup=await get_ikb_menu_client())
        else:
            await message.answer(f'Вы ввели неверный ТОКЕН, {clients_list}',
                                 reply_markup=await get_ikb_menu_other())
    await state.finish()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_callback_query_handler(set_new_user, text='registration')
    dp.register_message_handler(load_name, state=FSMRegistrationUser.name)
    dp.register_message_handler(load_token, state=FSMRegistrationUser.token)
