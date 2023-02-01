from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_ikb_menu_other() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Зарегистрироваться', callback_data='registration')],
        [InlineKeyboardButton('Информация о боте', callback_data='info_help')],
    ])

    return ikb
