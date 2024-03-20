from aiogram import types

from keyboards.inline import ikb_change
from utils.db_api import quick_commands as commands
from filters import IsPrivate
from keyboards.inline import ikb_start
from utils.misc import rate_limit
from loader import dp
from utils.db_api.quick_commands import get_score


@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text='/profile')
async def profile(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        score = await get_score(user.user_id)
        await message.answer(
                            f'Имя пользователя - {user.first_name} {user.last_name}\n'
                            f'Никнейм - {user.username}\n'
                            f'Счет - {score}', reply_markup=ikb_change)
    except Exception:
        await message.answer('У тебя еще нет профиля\n'
                             'Для создания профиля пройди регистрацию', reply_markup=ikb_start)
