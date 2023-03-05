from aiogram import types
from loader import dp


@dp.message_handler(text='Регистрация')
async def buttons_test(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}! \n'
                         f'Напиши свои имя и фамилию')

