from aiogram.types import CallbackQuery
import os
from keyboards.inline import ikb_start, ikb_game, ikb_game_start
from loader import dp
from aiogram import types

from utils.db_api import quick_commands as commands
from utils.db_api.test import select_random_image, get_dirname

PATH_TO_FILE = 'http://rodinka.lpt.digital/images/'


@dp.callback_query_handler(text='game')
async def command_game(message: types.Message):
    command_game.photo_url = None
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            command_game.photo_url = await select_random_image()
            path_to_file = os.path.join(PATH_TO_FILE + command_game.photo_url)
            await dp.bot.send_photo(chat_id=message.from_user.id, photo=path_to_file, reply_markup=ikb_game)
    except AttributeError:
        await message.answer(f'Привет, {message.from_user.first_name}!\n'
                             f'Сначала пройди регистрацию.', reply_markup=ikb_start)


@dp.callback_query_handler(text='mel')
async def mel(call: CallbackQuery):
    await call.message.edit_reply_markup(None)
    if await get_dirname(command_game.photo_url) == 'mel':
        await commands.update_score(call.message.chat.id)
        await call.message.answer('Верно\n Играть снова?', reply_markup=ikb_game_start)
        command_game.photo_url = None
    else:
        await call.message.answer('Неверно\n Играть снова?', reply_markup=ikb_game_start)


@dp.callback_query_handler(text='endgame')
async def endgame(call: CallbackQuery):
    await call.message.edit_reply_markup(None)
    await call.message.answer('Ты закончил игру')
    command_game.photo_url = None


@dp.callback_query_handler(text='akiec')
async def akiec(call: CallbackQuery):
    await call.message.edit_reply_markup(None)
    if await get_dirname(command_game.photo_url) == 'akiec':
        await commands.update_score(call.message.chat.id)
        await call.message.answer('Верно\n Играть снова?', reply_markup=ikb_game_start)
        command_game.photo_url = None
    else:
        await call.message.answer('Неверно\n Играть снова?', reply_markup=ikb_game_start)


@dp.callback_query_handler(text='bcc')
async def bcc(call: CallbackQuery):
    await call.message.edit_reply_markup(None)
    if await get_dirname(command_game.photo_url) == 'bcc':
        await commands.update_score(call.message.chat.id)
        await call.message.answer('Верно\n Играть снова?', reply_markup=ikb_game_start)
        command_game.photo_url = None
    else:
        await call.message.answer('Неверно\n Играть снова?', reply_markup=ikb_game_start)


@dp.callback_query_handler(text='bkl')
async def bkl(call: CallbackQuery):
    await call.message.edit_reply_markup(None)
    if await get_dirname(command_game.photo_url) == 'bkl':
        await commands.update_score(call.message.chat.id)
        await call.message.answer('Верно\n Играть снова?', reply_markup=ikb_game_start)
        command_game.photo_url = None
    else:
        await call.message.answer('Неверно\n Играть снова?', reply_markup=ikb_game_start)


@dp.callback_query_handler(text='df')
async def df(call: CallbackQuery):
    await call.message.edit_reply_markup(None)
    if await get_dirname(command_game.photo_url) == 'df':
        await commands.update_score(call.message.chat.id)
        await call.message.answer('Верно\n Играть снова?', reply_markup=ikb_game_start)
        command_game.photo_url = None
    else:
        await call.message.answer('Неверно\n Играть снова?', reply_markup=ikb_game_start)


@dp.callback_query_handler(text='nv')
async def nv(call: CallbackQuery):
    await call.message.edit_reply_markup(None)
    if await get_dirname(command_game.photo_url) == 'nv':
        await commands.update_score(call.message.chat.id)
        await call.message.answer('Верно\n Играть снова?', reply_markup=ikb_game_start)
        command_game.photo_url = None
    else:
        await call.message.answer('Неверно\n Играть снова?', reply_markup=ikb_game_start)


@dp.callback_query_handler(text='vasc')
async def vasc(call: CallbackQuery):
    await call.message.edit_reply_markup(None)
    if await get_dirname(command_game.photo_url) == 'vasc':
        await commands.update_score(call.message.chat.id)
        await call.message.answer('Верно\n Играть снова?', reply_markup=ikb_game_start)
        command_game.photo_url = None
    else:
        await call.message.answer('Неверно\n Играть снова?', reply_markup=ikb_game_start)
