from aiogram import types

from keyboards.inline import ikb_start, ikb_change
from loader import dp
from utils.misc import rate_limit
from utils.db_api import quick_commands as commands
from filters import IsPrivate
from aiogram.types import CallbackQuery


@rate_limit(limit=3, key='/start')
@dp.message_handler(IsPrivate(), text='/start')
async def command_start(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'Привет {user.first_name}\n'
                                 f'Ты уже зарегистрирован', reply_markup=ikb_change)
    except AttributeError:
        await message.answer(f'Добро пожаловать!\nSkin Education Bot -- может помочь в изучении кожных болезней '
                             f'и подобрать клинические рекомендации, теперь они собраны в одном месте.', reply_markup=ikb_start)

@dp.callback_query_handler(text='sub')
async def command_sub(call: CallbackQuery):
    await call.message.answer(f'Попробуйте все возможности бота бесплатно в течение 7 дней!'
                              f'\n\nЭтого времени достаточно, чтобы оценить полезность тренажеров, задач и материалов для изучения дерматологии.'
                              f'\n\nПосле окончания пробного периода вы можете оформить полноценную подписку на 3 месяца. '
                              f'Она позволит и дальше пользоваться всей базой знаний, новыми еженедельными кейсами и обновлениями тренажеров.'
                              f'\n\nСтоимость 3-месячного доступа - 200 рублей.'
                              f'\n\nОформите подписку, чтобы продолжить повышать свою квалификацию в удобном онлайн-режиме!')

