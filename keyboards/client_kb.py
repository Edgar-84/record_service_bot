from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_ikb_menu_client() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Отправить заявку на запись', callback_data='prepare_application')],
        [InlineKeyboardButton('Показать мои заявки', callback_data='view_client_records')],
    ])

    return ikb
