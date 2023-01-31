from aiogram.utils import executor
from init_bot import dp
from data.logger_settings import logger

from handlers import other


async def on_startup(_):
    logger.info('Bot Online')

other.register_handlers_other(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
