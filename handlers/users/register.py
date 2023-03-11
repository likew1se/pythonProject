from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import types

from filters import IsPrivate
from states import register

from loader import dp


@dp.message_handler(IsPrivate(), text='Регистрация')
async def register_(message: types.Message):

    await message.answer('Привет, ты начал регистрацию\nВведи свое имя')
    await register.test1.set()


@dp.message_handler(state=register.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test1=answer)
    await message.answer(f'{answer}, сколько тебе лет?')
    await register.test2.set()


@dp.message_handler(state=register.test2)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test2=answer)
    data = await state.get_data()
    name = data.get('test1')
    years = data.get('test2')
    await message.answer(f'Регистрация завершена\n'
                         f'Твое имя {name}\n'
                         f'Тебе {years}')
    await state.finish()