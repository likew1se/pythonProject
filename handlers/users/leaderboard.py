from aiogram import types
import numpy as np
from aiogram.types import CallbackQuery

from loader import dp
from utils.db_api import quick_commands as commands


@dp.callback_query_handler(text='leader')
async def show_lead(call: CallbackQuery):
    top = await commands.show_top()
    msg = ''
    id = 0
    count = 5
    for user_id, scr in top:
        id += 1
        if id <= count:
            user = await commands.select_user(user_id)
            if user:
                mention = f'<a href="tg://user?id={user.user_id}">{user.first_name}</a>'
                msg += f'{id}. {mention} - {scr}\n'
            else:
                id -= 1
        else:
            break
    await call.message.answer(f'Топ пользователей: \n{msg}')
