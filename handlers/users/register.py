from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline import ikb_change
from utils.db_api import quick_commands as commands
from filters import IsPrivate
from states import register

from loader import dp


@dp.callback_query_handler(text='reg')
async def register_(call: CallbackQuery):
    try:
        user = await commands.select_user(call.from_user.id)
        if user.status == 'active':
            await call.message.answer('Ты уже зарегистрирован')
    except AttributeError:
        await call.message.answer('Привет, ты начал регистрацию!\nВведи свое имя')
        await register.first_name.set()


@dp.message_handler(state=register.first_name)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(first_name=answer)
    await message.answer('Введи свою фамилию')
    await register.last_name.set()


@dp.message_handler(state=register.last_name)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(last_name=answer)
    data = await state.get_data()
    name = data.get('first_name')
    surname = data.get('last_name')
    await commands.add_user(user_id=message.from_user.id,
                            first_name=name,
                            last_name=surname,
                            username=message.from_user.username,
                            status='active',
                            score=0)
    await message.answer(f'Регистрация завершена\n'
                         f'Пользователь {name} {surname} создан', reply_markup=ikb_change)
    await state.finish()


