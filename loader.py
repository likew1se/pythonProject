from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils.db_api.db_gino import db

from data import config

import postgre as pg

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)


storage = MemoryStorage()


dp = Dispatcher(bot, storage=storage)


__all__ = ['bot', 'storage', 'dp', 'db']

# хандлеры из бот файла
# @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#    user_id = message.from_user.id
#    user_full_name = message.from_user.full_name
#    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
#    await message.answer(f'Привет, {user_full_name}!')
