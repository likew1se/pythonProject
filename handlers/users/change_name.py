from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from utils.db_api import quick_commands as commands
from states import new_register
from loader import dp


@dp.callback_query_handler(text='change')
async def change_name(call: CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    if user.status == 'active':
        await call.message.answer('Введи новое имя')
        await new_register.new_first_name.set()


@dp.message_handler(state=new_register.new_first_name)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(new_first_name=answer)
    await message.answer('Введи новую фамилию')
    await new_register.new_last_name.set()


@dp.message_handler(state=new_register.new_last_name)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(new_last_name=answer)
    data = await state.get_data()
    name = data.get('new_first_name')
    surname = data.get('new_last_name')
    await commands.update_name(user_id=message.from_user.id,
                               first_name=name,
                               last_name=surname)
    await message.answer(f'Профиль успешно изменен\n'
                         f'Твое новое имя: {name} {surname}')
    await state.finish()
