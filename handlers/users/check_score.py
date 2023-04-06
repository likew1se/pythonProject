from aiogram.types import CallbackQuery
from keyboards.inline import ikb_start, ikb_game_start
from loader import dp
from aiogram import types

from utils.db_api import quick_commands as commands
from utils.db_api.quick_commands import get_score


@dp.callback_query_handler(text='check')
async def show_score(call: CallbackQuery):
    try:
        user = await commands.select_user(call.message.chat.id)
        if user.status == 'active':
            score = await get_score(user.user_id)
            await call.message.answer(f'Твой счет: {score}', reply_markup=ikb_game_start)
    except AttributeError:
        await call.message.answer(f'Привет, {call.message.from_user.first_name}!\n'
                             f'Сначала пройди регистрацию.', reply_markup=ikb_start)
