from aiogram import types
from loader import dp
from utils.db_api import quick_commands as commands


@dp.message_handler(text='/help')
async def command_help(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}!')
