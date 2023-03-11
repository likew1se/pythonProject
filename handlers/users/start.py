from aiogram import types
from loader import dp
from utils.misc import rate_limit

from filters import IsPrivate


@rate_limit(limit=3, key='/start')
@dp.message_handler(IsPrivate(), text='/start')
async def command_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}! \n'
                         f'Твой id: {message.from_user.id}')
