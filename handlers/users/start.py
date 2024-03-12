from aiogram import types

from keyboards.inline import ikb_start, ikb_change
from loader import dp
from utils.misc import rate_limit
from utils.db_api import quick_commands as commands
from filters import IsPrivate


@rate_limit(limit=3, key='/start')
@dp.message_handler(IsPrivate(), text='/start')
async def command_start(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'Привет {user.first_name}\n'
                                 f'Ты уже зарегистрирован', reply_markup=ikb_start)
    except AttributeError:
        await message.answer(f'Привет, {message.from_user.first_name}!', reply_markup=ikb_start)


