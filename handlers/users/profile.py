from aiogram import types

from filters import IsPrivate
from keyboards.inline import ikb_start
from utils.misc import rate_limit
from loader import dp
from utils.db_api import quick_commands as commands


@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text='/profile')
async def profile(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        await message.answer(f'Айди - {user.user_id}\n'
                            f'first_name - {user.first_name}\n'
                            f'last_nanme - {user.last_name}\n'
                            f'username - {user.username}\n'
                            f'status - {user.status}')
    except Exception:
        await message.answer('У тебя еще нет профиля\n'
                             'Для создания профиля пройди регистрацию', reply_markup=ikb_start)