from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram import types
from states import dermatit, akne
from loader import dp


@dp.callback_query_handler(text='oprosnik')
async def oprosnik(call: CallbackQuery):
    await call.message.answer(f'АТОПИЧЕСКИЙ ДЕРМАТИТ')
    await call.message.answer(f'2. Выраженность'
                              f'\n\nА) Оцените выраженность покраснения (эритемы):'
                              f'\n\n0-отсутствие проявлений'
                              f'\n1- Слабые проявления'
                              f'\n2- Умеренные проявления'
                              f'\n3-тяжелые проявления')
    await dermatit.dq1.set()


@dp.message_handler(state=dermatit.dq1)
async def q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(dq1=answer)
    await message.answer(f'Б) Оцените выраженность отека/папулы:'
                         f'\n\n0-отсутствие проявлений'
                         f'\n1- Слабые проявления'
                         f'\n2- Умеренные проявления'
                         f'\n3- 3-тяжелые проявления')
    await dermatit.dq2.set()


@dp.message_handler(state=dermatit.dq2)
async def q2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(dq2=answer)
    await message.answer(f'В) Оцените выраженность мокнутия/корки:'
                         f'\n\n0-отсутствие проявлений'
                         f'\n1- Слабые проявления'
                         f'\n2- Умеренные проявления'
                         f'\n3- 3-тяжелые проявления')
    await dermatit.dq3.set()


@dp.message_handler(state=dermatit.dq3)
async def q3(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(dq3=answer)
    await message.answer(f'Г) Оцените выраженность расчесов (экскориации):'
                         f'\n\n0-отсутствие проявлений'
                         f'\n1- Слабые проявления'
                         f'\n2- Умеренные проявления'
                         f'\n3- 3-тяжелые проявления')
    await dermatit.dq4.set()


@dp.message_handler(state=dermatit.dq4)
async def q4(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(dq4=answer)
    await message.answer(f'Д) Оцените выраженность утолщения кожи и усиление кожного рисунка(лихенификации): '
                         f'\n\n0-отсутствие проявлений'
                         f'\n1- Слабые проявления'
                         f'\n2- Умеренные проявления'
                         f'\n3- 3-тяжелые проявления')
    await dermatit.dq5.set()


@dp.message_handler(state=dermatit.dq5)
async def q5(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(dq5=answer)
    await message.answer(f'Е) Оцените сухость непораженных участков кожи: '
                         f'\n\n0-отсутствие проявлений'
                         f'\n1- Слабые проявления'
                         f'\n2- Умеренные проявления'
                         f'\n3- 3-тяжелые проявления')
    await dermatit.dq6.set()


@dp.message_handler(state=dermatit.dq6)
async def q6(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(dq6=answer)
    await message.answer(f'3.  Оцените зуд по шкале от 1 до 10')
    await dermatit.dq7.set()


@dp.message_handler(state=dermatit.dq7)
async def q7(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(dq7=answer)
    await message.answer(f'4.  Оцените нарушение сна по шкале от 1 до 10')
    await dermatit.dq8.set()


@dp.message_handler(state=dermatit.dq8)
async def q8(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(dq8=answer)
    await message.answer(f'АКНЕ')
    await message.answer(f'Оцените выраженность акне '
                         f'\n\n0 – кожа практически чистая, наблюдается максимум три элемента, заметных с близкого расстояния'
                         f'\n1 – на 1/4 поверхности лица наблюдаются небольшие прыщи или черные точки, почти незаметны с расстояния 2,5 м'
                         f'\n2 – на ½ поверхности наблюдаются прыщи и черные точки ИЛИ несколько крупных выступающих прыщей'
                         f'\n3 – ¾ поверхности занимают прыщи и/или черные точки, имеются многочисленные элементы с гноем'
                         f'\n4 – поражена практически вся поверхность лица, наличие узлов ')
    await akne.aq1.set()



@dp.message_handler(state=akne.aq1)
async def aq1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(aq1=answer)
    await message.answer(f'Оцените нарушения трудоспособности при акне'
                         f'\n\n1. Испытывали ли вы на протяжении предыдущего месяца чувство агрессивности, отчаяния, смущения из-за того, что у вас акне?'
                         f'\n0 – да, в значительной степени'
                         f'\n1- Часто'
                         f'\n2- Немного'
                         f'\n3- совсем нет')
    await akne.aq2.set()


@dp.message_handler(state=akne.aq2)
async def aq2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(aq2=answer)
    await message.answer(f'2. Мешало ли акне в предыдущий месяц вашему повседневному общению, встречам, отношениям с противоположным полом?'
                         f'\n0 – очень сильно мешало'
                         f'\n1 – в большинстве случаев мешало'
                         f'\n2 – иногда или в некоторых случаях'
                         f'\n3 – не мешало')
    await akne.aq3.set()



@dp.message_handler(state=akne.aq3)
async def aq3(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(aq3=answer)
    await message.answer(f'3. Избегали ли вы купания/ переодевания в общественных раздевалках'
                         f'\n0 – Все время'
                         f'\n1 – В большинстве случаев'
                         f'\n2 – Иногда'
                         f'\n3 – Совсем нет')
    await akne.aq4.set()


@dp.message_handler(state=akne.aq4)
async def aq4(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(aq4=answer)
    await message.answer(f'4. Вызывает ли у вас беспокойство ваш внешний вид'
                         f'\n0 – Очень сильное беспокойство каждый день'
                         f'\n1 – Часто'
                         f'\n2 – Иногда'
                         f'\n3 – Совсем нет')
    await akne.aq5.set()


@dp.message_handler(state=akne.aq5)
async def aq5(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(aq5=answer)
    await message.answer(f'5. Насколько тяжелой проблемой для вас сейчас является акне'
                         f'\n0- Самое худшее из всех возможных состояний'
                         f'\n1- Очень большая проблема'
                         f'\n2- Второстепенная проблема'
                         f'\n3- Вообще не проблема')
    await akne.aq6.set()


@dp.message_handler(state=akne.aq6)
async def aq6(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(aq6=answer)
    await state.finish()