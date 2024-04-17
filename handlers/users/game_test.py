from aiogram.types import CallbackQuery
import os
from keyboards.inline import ikb_start, ikb_game, ikb_game_start, ikb_change
from loader import dp
from aiogram import types
from data.config import DISEASE_NAME as dn

from utils.db_api import quick_commands as commands
from utils.db_api.test import select_random_image, get_dirname

PATH_TO_FILE = 'http://rodinka.lpt.digital/images/'
MEL = dn['mel']
AKIEC = dn['akiec']
BCC = dn['bcc']
BKL = dn['bkl']
DF = dn['df']
NV = dn['nv']
VASC = dn['vasc']

user_dict = {}


@dp.callback_query_handler(text='game')
async def command_game(call: CallbackQuery):
    command_game.photo_url = None
    try:
        user = await commands.select_user(call.message.chat.id)
        if user.status == 'active':
            command_game.photo_url = await select_random_image()
            user_dict[user.first_name] = command_game.photo_url
            path_to_file = os.path.join(PATH_TO_FILE + user_dict[user.first_name])
            await dp.bot.send_photo(chat_id=call.message.chat.id, photo=path_to_file, reply_markup=ikb_game)
            dirname = await get_dirname(user_dict[user.first_name])
            print(path_to_file, dirname)
    except AttributeError:
        await call.message.answer(f'Привет, {call.message.chat.id.first_name}!\n'
                             f'Сначала пройди регистрацию.', reply_markup=ikb_start)


@dp.callback_query_handler(text='mel')
async def mel(call: CallbackQuery):
    await call.message.edit_reply_markup(None)
    user = await commands.select_user(call.message.chat.id)
    dirname = await get_dirname(user_dict[user.first_name])
    if dirname == 'mel':
        await commands.update_score(call.message.chat.id)
        await call.message.answer(f'Верно, это {MEL} \nИграть снова?', reply_markup=ikb_game_start)
        command_game.photo_url = None
    else:
        await call.message.answer(f'Неверно, это {dn[dirname]}\nИграть снова?',
                                  reply_markup=ikb_game_start)


@dp.callback_query_handler(text='akiec')
async def akiec(call: CallbackQuery):
    await call.message.edit_reply_markup(None)
    user = await commands.select_user(call.message.chat.id)
    dirname = await get_dirname(user_dict[user.first_name])
    if dirname == 'akiec':
        await commands.update_score(call.message.chat.id)
        await call.message.answer(f'Верно, это {AKIEC}\nИграть снова?', reply_markup=ikb_game_start)
        command_game.photo_url = None
    else:
        await call.message.answer(f'Неверно, это {dn[dirname]}\nИграть снова?', reply_markup=ikb_game_start)


@dp.callback_query_handler(text='bcc')
async def bcc(call: CallbackQuery):
    await call.message.edit_reply_markup(None)
    user = await commands.select_user(call.message.chat.id)
    dirname = await get_dirname(user_dict[user.first_name])
    if dirname == 'bcc':
        await commands.update_score(call.message.chat.id)
        await call.message.answer(f'Верно, это {BCC}\nИграть снова?', reply_markup=ikb_game_start)
        command_game.photo_url = None
    else:
        await call.message.answer(f'Неверно, это {dn[dirname]}\nИграть снова?', reply_markup=ikb_game_start)


@dp.callback_query_handler(text='bkl')
async def bkl(call: CallbackQuery):
    await call.message.edit_reply_markup(None)
    user = await commands.select_user(call.message.chat.id)
    dirname = await get_dirname(user_dict[user.first_name])
    if dirname == 'bkl':
        await commands.update_score(call.message.chat.id)
        await call.message.answer(f'Верно, это {BKL}\nИграть снова?', reply_markup=ikb_game_start)
        command_game.photo_url = None
    else:
        await call.message.answer(f'Неверно, это {dn[dirname]}\nИграть снова?', reply_markup=ikb_game_start)

@dp.callback_query_handler(text='df')
async def df(call: CallbackQuery):
    await call.message.edit_reply_markup(None)
    user = await commands.select_user(call.message.chat.id)
    dirname = await get_dirname(user_dict[user.first_name])
    if dirname == 'df':
        await commands.update_score(call.message.chat.id)
        await call.message.answer(f'Верно, это {DF}\nИграть снова?', reply_markup=ikb_game_start)
        command_game.photo_url = None
    else:
        await call.message.answer(f'Неверно, это {dn[dirname]}\nИграть снова?', reply_markup=ikb_game_start)


@dp.callback_query_handler(text='nv')
async def nv(call: CallbackQuery):
    await call.message.edit_reply_markup(None)
    user = await commands.select_user(call.message.chat.id)
    dirname = await get_dirname(user_dict[user.first_name])
    if dirname == 'nv':
        await commands.update_score(call.message.chat.id)
        await call.message.answer(f'Верно, это {NV}\nИграть снова?', reply_markup=ikb_game_start)
        command_game.photo_url = None
    else:
        await call.message.answer(f'Неверно, это {dn[dirname]}\nИграть снова?', reply_markup=ikb_game_start)


@dp.callback_query_handler(text='vasc')
async def vasc(call: CallbackQuery):
    await call.message.edit_reply_markup(None)
    user = await commands.select_user(call.message.chat.id)
    dirname = await get_dirname(user_dict[user.first_name])
    if dirname == 'vasc':
        await commands.update_score(call.message.chat.id)
        await call.message.answer(f'Верно, это {VASC}\nИграть снова?', reply_markup=ikb_game_start)
        command_game.photo_url = None
    else:
        await call.message.answer(f'Неверно, это {dn[dirname]}\nИграть снова?', reply_markup=ikb_game_start)


@dp.callback_query_handler(text='endgame')
async def endgame(call: CallbackQuery):
    await call.message.edit_reply_markup(None)
    await call.message.answer('Ты закончил игру', reply_markup=ikb_change)
    user = await commands.select_user(call.message.chat.id)
    user_dict[user.first_name] = None
    command_game.photo_url = None

