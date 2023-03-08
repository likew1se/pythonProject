from loader import dp
from keyboards.default import kb_menu
from aiogram.dispatcher.filters import Command
from aiogram import types


@dp.message_handler(text='Меню')
async def menu(message: types.Message):
    await message.answer('Выбери пункт из меню', reply_markup=kb_menu)