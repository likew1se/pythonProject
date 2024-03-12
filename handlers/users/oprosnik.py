from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram import types
from states import oprosnik
from loader import dp
from utils import answers_temp


@dp.callback_query_handler(text='opros')
async def instruction(call: CallbackQuery):
    await call.message.answer(f'1. образование кровоточит?')
    await oprosnik.q1.set()


@dp.message_handler(state=oprosnik.q1)
async def q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(q1=answer)
    await message.answer(f'2. Образование имеет ровные края?')
    await oprosnik.q2.set()


@dp.message_handler(state=oprosnik.q2)
async def q2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(q2=answer)
    await message.answer(f'3. Образование имеет неравномерный цвет, то есть определяются более светлые или более темные участки или вкрапления?')
    await oprosnik.q3.set()


@dp.message_handler(state=oprosnik.q3)
async def q3(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(q3=answer)
    await message.answer(f'4. Образование увеличилось в размерах со времени последней диагностики?')
    await oprosnik.q4.set()


@dp.message_handler(state=oprosnik.q4)
async def q4(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(q4=answer)
    await message.answer(f'5. Имеет ли образование корочку на своей поверхности?')
    await oprosnik.q5.set()


@dp.message_handler(state=oprosnik.q5)
async def q5(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(q5=answer)
    await message.answer(f'6. Изменилось ли образование наощупь в последнее время?')
    await oprosnik.q6.set()


@dp.message_handler(state=oprosnik.q6)
async def q6(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(q6=answer)
    await message.answer(f'7. Испытываете ли Вы ощущение зуда в области образования?')
    await oprosnik.q7.set()


@dp.message_handler(state=oprosnik.q7)
async def q7(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(q7=answer)
    await message.answer(f'8. Испытываете ли Вы болезненные ощущения в области образования?')
    await oprosnik.q8.set()


@dp.message_handler(state=oprosnik.q8)
async def q8(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(q8=answer)
    data = await state.get_data()
    a1 = data.get('q1')
    a2 = data.get('q2')
    a3 = data.get('q3')
    a4 = data.get('q4')
    a5 = data.get('q5')
    a6 = data.get('q6')
    a7 = data.get('q7')
    a8 = data.get('q8')

